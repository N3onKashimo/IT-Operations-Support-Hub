import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date
from utils.data_loader import load_csv

st.title("Request / Incident Intake")
st.caption("Submit a new service request or incident.")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REQUESTS_FILE = DATA_DIR / "requests.csv"

kb_df = load_csv("kb_articles.csv")
assets_df = load_csv("assets.csv")

categories = [
    "Accounts & Access",
    "Workstation Setup",
    "Printing & Peripherals",
    "Network / Wi-Fi",
    "Software / Application Support",
    "Remote Support",
    "Internal Tools"
]

subcategories_map = {
    "Accounts & Access": ["New User Account", "Password Reset / Unlock", "Access Change"],
    "Workstation Setup": ["New Device Setup", "Reimage / Rebuild", "Hardware Issue"],
    "Printing & Peripherals": ["Printer Issue", "Peripheral Setup", "Scanner Issue"],
    "Network / Wi-Fi": ["Wi-Fi Issue", "VPN Issue", "Network Access"],
    "Software / Application Support": ["Software Install", "Application Error", "License Request"],
    "Remote Support": ["Remote Troubleshooting", "Screen Share Support"],
    "Internal Tools": ["Internal Portal Issue", "JIRA / Ticketing", "Access to Internal Tool"]
}

priority_options = ["Low", "Medium", "High", "Critical"]
request_type_options = ["Service Request", "Incident"]

def generate_request_id(existing_df: pd.DataFrame) -> str:
    if existing_df.empty or "request_id" not in existing_df.columns:
        return "R-1001"
    existing_ids = existing_df["request_id"].dropna().astype(str).tolist()
    numeric_parts = []
    for rid in existing_ids:
        if rid.startswith("R-"):
            try:
                numeric_parts.append(int(rid.split("-")[1]))
            except Exception:
                pass
    next_num = max(numeric_parts, default=1000) + 1
    return f"R-{next_num}"

existing_requests_df = load_csv("requests.csv")

with st.form("request_intake_form"):
    st.markdown("### Request Basics")
    col1, col2 = st.columns(2)
    request_type = col1.selectbox("Request Type", request_type_options)
    category = col2.selectbox("Category", categories)

    subcategory = st.selectbox("Subcategory", subcategories_map.get(category, []))
    title = st.text_input("Title")
    description = st.text_area("Description", height=120)

    st.markdown("### Requester Information")
    col3, col4 = st.columns(2)
    requested_by = col3.text_input("Requested By")
    requested_for = col4.text_input("Requested For")

    col5, col6 = st.columns(2)
    department = col5.text_input("Department")
    location = col6.text_input("Location")

    st.markdown("### Support Details")
    asset_options = [""] + assets_df["asset_id"].dropna().astype(str).tolist() if not assets_df.empty else [""]
    asset_id = st.selectbox("Asset ID (Optional)", asset_options)

    col7, col8 = st.columns(2)
    priority = col7.selectbox("Priority", priority_options, index=1)
    due_date = col8.date_input("Due Date", value=date.today())

    kb_options = [""] + kb_df["article_id"].dropna().astype(str).tolist() if not kb_df.empty else [""]
    knowledge_article_id = st.selectbox("Related KB Article (Optional)", kb_options)

    submitted = st.form_submit_button("Submit Request")

if submitted:
    if not title.strip() or not description.strip() or not requested_by.strip():
        st.error("Please complete Title, Description, and Requested By.")
    else:
        request_id = generate_request_id(existing_requests_df)

        assigned_group_map = {
            "Accounts & Access": "Service Desk",
            "Workstation Setup": "Desktop Support",
            "Printing & Peripherals": "Desktop Support",
            "Network / Wi-Fi": "Infrastructure",
            "Software / Application Support": "Desktop Support",
            "Remote Support": "Service Desk",
            "Internal Tools": "Applications Support"
        }

        new_row = {
            "request_id": request_id,
            "submitted_date": date.today().isoformat(),
            "request_type": request_type,
            "category": category,
            "subcategory": subcategory,
            "title": title.strip(),
            "description": description.strip(),
            "requested_by": requested_by.strip(),
            "department": department.strip(),
            "location": location.strip(),
            "asset_id": asset_id,
            "priority": priority,
            "status": "Open",
            "assigned_group": assigned_group_map.get(category, "Service Desk"),
            "knowledge_article_id": knowledge_article_id,
            "requested_for": requested_for.strip(),
            "due_date": due_date.isoformat(),
            "resolution_notes": "",
            "closed_date": ""
        }

        updated_df = pd.concat([existing_requests_df, pd.DataFrame([new_row])], ignore_index=True)
        updated_df.to_csv(REQUESTS_FILE, index=False)

        st.success(f"Request submitted successfully. New Request ID: {request_id}")
        st.dataframe(pd.DataFrame([new_row]), use_container_width=True)