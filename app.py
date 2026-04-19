import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="IT Operations Support Hub", layout="wide")

st.title("IT Operations Support Hub")
st.caption("Lightweight internal IT support portal MVP built with Python + Streamlit")

st.markdown("""
This project simulates a small internal IT support portal with:
- Knowledge Base
- Service Catalog
- Request / Incident Intake
- Accounts & Access workflows
""")

col1, col2, col3 = st.columns(3)
col1.metric("Open Requests", "0")
col2.metric("KB Articles", "0")
col3.metric("Catalog Services", "0")

st.info("Use the sidebar to navigate through the MVP pages.")
