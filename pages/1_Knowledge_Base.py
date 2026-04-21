import streamlit as st
from utils.data_loader import load_csv

st.title("Knowledge Base")
st.caption("Browse internal support articles and quick-help documentation.")

kb_df = load_csv("kb_articles.csv")

if kb_df.empty:
    st.warning("No knowledge base articles found.")
    st.stop()

search_term = st.text_input("Search articles", placeholder="Try: password, printer, onboarding")

categories = ["All"] + sorted(kb_df["category"].dropna().unique().tolist())
selected_category = st.selectbox("Filter by category", categories)

filtered_df = kb_df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

if search_term:
    search_lower = search_term.lower()
    filtered_df = filtered_df[
        filtered_df["title"].fillna("").str.lower().str.contains(search_lower) |
        filtered_df["summary"].fillna("").str.lower().str.contains(search_lower) |
        filtered_df["keywords"].fillna("").str.lower().str.contains(search_lower)
    ]

st.metric("Matching Articles", len(filtered_df))

if filtered_df.empty:
    st.info("No matching articles found.")
else:
    for _, row in filtered_df.iterrows():
        with st.container():
            st.subheader(row["title"])
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.write(f"**Category:** {row['category']}")
            col2.write(f"**Audience:** {row['audience']}")
            col3.write(f"**Status:** {row['status']}")
            st.write(row["summary"])
            st.caption(f"Keywords: {row['keywords']}")
            st.markdown("---")