import streamlit as st
from utils.data_loader import load_csv

st.title("Service Catalog")
st.caption("Browse standard IT services, request types, and support offerings.")

services_df = load_csv("service_catalog.csv")

if services_df.empty:
    st.warning("No service catalog data found.")
    st.stop()

search_term = st.text_input("Search services", placeholder="Try: password, printer, software")

categories = ["All"] + sorted(services_df["category"].dropna().unique().tolist())
selected_category = st.selectbox("Filter by category", categories)

filtered_df = services_df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

if search_term:
    search_lower = search_term.lower()
    filtered_df = filtered_df[
        filtered_df["service_name"].fillna("").str.lower().str.contains(search_lower) |
        filtered_df["description"].fillna("").str.lower().str.contains(search_lower) |
        filtered_df["request_type"].fillna("").str.lower().str.contains(search_lower)
    ]

st.metric("Matching Services", len(filtered_df))

if filtered_df.empty:
    st.info("No matching services found.")
else:
    for _, row in filtered_df.iterrows():
        with st.container():
            st.subheader(row["service_name"])

            col1, col2, col3 = st.columns(3)
            col1.write(f"**Category:** {row['category']}")
            col2.write(f"**Request Type:** {row['request_type']}")
            col3.write(f"**Status:** {row['status']}")

            st.write(row["description"])

            col4, col5, col6 = st.columns(3)
            col4.write(f"**Target Fulfillment (Days):** {row['target_fulfillment_days']}")
            col5.write(f"**Requires Approval:** {row['requires_approval']}")
            approval_role = row["approval_role"] if str(row["approval_role"]).strip() else "N/A"
            col6.write(f"**Approval Role:** {approval_role}")

            kb_id = row["knowledge_article_id"] if str(row["knowledge_article_id"]).strip() else "N/A"
            st.caption(f"Related KB Article: {kb_id}")
            st.markdown("---")