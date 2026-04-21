import streamlit as st
from utils.data_loader import load_csv

st.title("Request Dashboard")
st.caption("Simple support workload visibility and request reporting.")

requests_df = load_csv("requests.csv")

if requests_df.empty:
    st.warning("No request data found.")
    st.stop()

total_requests = len(requests_df)
open_requests = len(requests_df[requests_df["status"] == "Open"]) if "status" in requests_df.columns else 0
closed_requests = len(requests_df[requests_df["status"] == "Closed"]) if "status" in requests_df.columns else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Requests", total_requests)
col2.metric("Open Requests", open_requests)
col3.metric("Closed Requests", closed_requests)

st.markdown("### Requests by Category")
if "category" in requests_df.columns:
    category_counts = requests_df["category"].value_counts()
    st.bar_chart(category_counts)

st.markdown("### Requests by Priority")
if "priority" in requests_df.columns:
    priority_counts = requests_df["priority"].value_counts()
    st.bar_chart(priority_counts)

st.markdown("### Requests by Type")
if "request_type" in requests_df.columns:
    type_counts = requests_df["request_type"].value_counts()
    st.bar_chart(type_counts)

st.markdown("### Recent Requests")
display_cols = [
    col for col in [
        "request_id",
        "submitted_date",
        "request_type",
        "category",
        "title",
        "priority",
        "status",
        "assigned_group"
    ] if col in requests_df.columns
]

st.dataframe(
    requests_df.sort_values(by="submitted_date", ascending=False)[display_cols],
    use_container_width=True
)