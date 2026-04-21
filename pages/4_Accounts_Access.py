import streamlit as st
from pathlib import Path
from utils.data_loader import load_csv

st.title("Accounts & Access")
st.caption("Identity, onboarding, offboarding, and access support workflows.")

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"

def read_markdown_file(filename: str) -> str:
    file_path = DOCS_DIR / filename
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return f"Could not load {filename}"

users_roles_df = load_csv("users_roles.csv")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "New User Account",
    "Password Reset / Unlock",
    "Access Change",
    "Runbooks",
    "Role Access Matrix"
])

with tab1:
    st.subheader("New User Account Request")
    st.write("Use this workflow when onboarding a new employee or contractor requiring standard system access.")

    st.markdown("""
**Required Request Details**
- Employee full name
- Start date
- Department
- Manager
- Job title / role
- Location
- Laptop required or not
- VPN required or not
- Any role-specific application access
""")

    st.markdown("### Onboarding Checklist")
    st.markdown(read_markdown_file("onboarding-runbook.md"))

with tab2:
    st.subheader("Password Reset / Unlock")
    st.write("Use this path for locked accounts, expired passwords, or sign-in troubleshooting.")

    st.markdown("""
**Basic Guidance**
1. Verify the user’s identity
2. Confirm whether the issue is reset, unlock, or MFA-related
3. Perform the reset/unlock action
4. Ask the user to test access
5. Document the outcome
""")

    st.markdown("### Password Reset Runbook")
    st.markdown(read_markdown_file("password-reset-runbook.md"))

with tab3:
    st.subheader("Access Change Request")
    st.write("Use this workflow for access additions, removals, or role changes.")

    st.markdown("""
**Typical Access Change Scenarios**
- Department transfer
- Application access needed for new responsibilities
- Shared drive or folder access
- Removal of access no longer required
- Temporary elevated permissions with approval
""")

    st.markdown("""
**Suggested Required Fields**
- Employee name
- Current role
- Requested access change
- Business justification
- Manager approval
- Effective date
""")

with tab4:
    st.subheader("Runbooks")
    st.markdown("### Onboarding")
    st.markdown(read_markdown_file("onboarding-runbook.md"))

    st.markdown("### Offboarding")
    st.markdown(read_markdown_file("offboarding-runbook.md"))

with tab5:
    st.subheader("Role Access Matrix")
    st.markdown(read_markdown_file("role-access-matrix.md"))

    st.markdown("### Users / Role Profiles")
    if users_roles_df.empty:
        st.info("No users/roles data found.")
    else:
        st.dataframe(users_roles_df, use_container_width=True)