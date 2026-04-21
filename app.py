import streamlit as st
import pandas as pd
from pathlib import Path

# Page config
st.set_page_config(page_title="IT Operations Support Hub", layout="wide")

st.title("IT Operations Support Hub")
st.caption("Lightweight internal IT support portal MVP")

# --- Data Paths ---
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

requests_file = DATA_DIR / "requests.csv"
kb_file = DATA_DIR / "kb_articles.csv"
services_file = DATA_DIR / "service_catalog.csv"

# --- Load Data ---
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except:
        return pd.DataFrame()

requests_df = load_csv(requests_file)
kb_df = load_csv(kb_file)
services_df = load_csv(services_file)

# --- Metrics ---
total_requests = len(requests_df)

open_requests = len(
    requests_df[requests_df["status"] == "Open"]
) if not requests_df.empty else 0

kb_count = len(kb_df)
service_count = len(services_df)

# --- Display Metrics ---
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", total_requests)
col2.metric("Open Requests", open_requests)
col3.metric("KB Articles", kb_count)
col4.metric("Services", service_count)

# --- Info Section ---
st.markdown("### About This Project")

st.markdown("""
This project simulates an internal IT support portal used to manage:
- Service requests
- Incident tracking
- Knowledge base articles
- Account and access workflows

Built using Python + Streamlit as a lightweight MVP.
""")