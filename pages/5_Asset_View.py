import streamlit as st
from utils.data_loader import load_csv

st.title("Asset View")
st.caption("Lookup internal devices and basic endpoint inventory information.")

assets_df = load_csv("assets.csv")

if assets_df.empty:
    st.warning("No asset data found.")
    st.stop()

search_term = st.text_input("Search assets", placeholder="Try: laptop, finance, ENG-DT-07")

asset_types = ["All"] + sorted(assets_df["asset_type"].dropna().unique().tolist())
departments = ["All"] + sorted(assets_df["department"].dropna().unique().tolist())
statuses = ["All"] + sorted(assets_df["status"].dropna().unique().tolist())

col1, col2, col3 = st.columns(3)
selected_asset_type = col1.selectbox("Filter by Asset Type", asset_types)
selected_department = col2.selectbox("Filter by Department", departments)
selected_status = col3.selectbox("Filter by Status", statuses)

filtered_df = assets_df.copy()

if selected_asset_type != "All":
    filtered_df = filtered_df[filtered_df["asset_type"] == selected_asset_type]

if selected_department != "All":
    filtered_df = filtered_df[filtered_df["department"] == selected_department]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df["status"] == selected_status]

if search_term:
    search_lower = search_term.lower()
    filtered_df = filtered_df[
        filtered_df["asset_id"].fillna("").astype(str).str.lower().str.contains(search_lower) |
        filtered_df["asset_tag"].fillna("").astype(str).str.lower().str.contains(search_lower) |
        filtered_df["assigned_to"].fillna("").astype(str).str.lower().str.contains(search_lower) |
        filtered_df["device_name"].fillna("").astype(str).str.lower().str.contains(search_lower) |
        filtered_df["notes"].fillna("").astype(str).str.lower().str.contains(search_lower)
    ]

st.metric("Matching Assets", len(filtered_df))
st.dataframe(filtered_df, use_container_width=True)