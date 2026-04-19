param(
    [string]$ProjectName = "it-operations-support-hub"
)

$root = Join-Path (Get-Location) $ProjectName

# Create root
New-Item -Path $root -ItemType Directory -Force | Out-Null

# Create folders
@(
    "pages",
    "data",
    "docs",
    "utils",
    "screenshots",
    ".streamlit"
) | ForEach-Object {
    New-Item -Path (Join-Path $root $_) -ItemType Directory -Force | Out-Null
}

# Create files
@(
    "app.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    ".streamlit\config.toml",
    "pages\1_Knowledge_Base.py",
    "pages\2_Service_Catalog.py",
    "pages\3_Request_Incident_Intake.py",
    "pages\4_Accounts_Access.py",
    "pages\5_Asset_View.py",
    "pages\6_Request_Dashboard.py",
    "data\assets.csv",
    "data\requests.csv",
    "data\kb_articles.csv",
    "data\users_roles.csv",
    "data\service_catalog.csv",
    "docs\onboarding-runbook.md",
    "docs\offboarding-runbook.md",
    "docs\password-reset-runbook.md",
    "docs\role-access-matrix.md",
    "utils\data_loader.py",
    "utils\constants.py",
    "utils\forms.py"
) | ForEach-Object {
    New-Item -Path (Join-Path $root $_) -ItemType File -Force | Out-Null
}

# requirements.txt
@"
streamlit
pandas
"@ | Set-Content -Path (Join-Path $root "requirements.txt")

# .gitignore
@"
__pycache__/
*.pyc
.venv/
.env
.streamlit/secrets.toml
"@ | Set-Content -Path (Join-Path $root ".gitignore")

# Streamlit config
@"
[theme]
base="dark"
"@ | Set-Content -Path (Join-Path $root ".streamlit\config.toml")

# app.py starter
@"
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
"@ | Set-Content -Path (Join-Path $root "app.py")

# page starters
@"
import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Knowledge Base")
st.write("Search and browse internal support articles.")
"@ | Set-Content -Path (Join-Path $root "pages\1_Knowledge_Base.py")

@"
import streamlit as st
import pandas as pd

st.title("Service Catalog")
st.write("Browse standard IT services and request types.")
"@ | Set-Content -Path (Join-Path $root "pages\2_Service_Catalog.py")

@"
import streamlit as st
import pandas as pd

st.title("Request / Incident Intake")
st.write("Submit a new request or incident.")
"@ | Set-Content -Path (Join-Path $root "pages\3_Request_Incident_Intake.py")

@"
import streamlit as st

st.title("Accounts & Access")
st.write("Access workflows, onboarding, offboarding, and role guidance.")
"@ | Set-Content -Path (Join-Path $root "pages\4_Accounts_Access.py")

@"
import streamlit as st

st.title("Asset View")
st.write("Optional page for asset visibility.")
"@ | Set-Content -Path (Join-Path $root "pages\5_Asset_View.py")

@"
import streamlit as st

st.title("Request Dashboard")
st.write("Optional page for metrics and reporting.")
"@ | Set-Content -Path (Join-Path $root "pages\6_Request_Dashboard.py")

# CSV headers
"asset_id,asset_tag,asset_type,assigned_to,department,location,device_name,serial_number,os,status,purchase_date,warranty_end,notes" |
    Set-Content -Path (Join-Path $root "data\assets.csv")

"request_id,submitted_date,request_type,category,subcategory,title,description,requested_by,department,location,asset_id,priority,status,assigned_group,knowledge_article_id,requested_for,due_date,resolution_notes,closed_date" |
    Set-Content -Path (Join-Path $root "data\requests.csv")

"article_id,title,category,summary,keywords,audience,last_updated,owner,status,link_slug" |
    Set-Content -Path (Join-Path $root "data\kb_articles.csv")

"user_id,full_name,department,job_title,location,manager_name,email,employment_status,role_profile,default_access,laptop_required,vpn_required,mfa_required,notes" |
    Set-Content -Path (Join-Path $root "data\users_roles.csv")

"service_id,service_name,category,request_type,description,target_fulfillment_days,requires_approval,approval_role,knowledge_article_id,status" |
    Set-Content -Path (Join-Path $root "data\service_catalog.csv")

# Markdown starter docs
@"
# Onboarding Runbook

## Purpose
Standard onboarding steps for a new employee.

## Checklist
- Confirm start date and manager
- Create account
- Assign standard access
- Confirm MFA
- Prepare workstation
- Validate software access
"@ | Set-Content -Path (Join-Path $root "docs\onboarding-runbook.md")

@"
# Offboarding Runbook

## Purpose
Standard offboarding and access removal steps.

## Checklist
- Confirm termination date
- Disable account
- Remove group/application access
- Recover assigned assets
- Document completion
"@ | Set-Content -Path (Join-Path $root "docs\offboarding-runbook.md")

@"
# Password Reset Runbook

## Purpose
Guide for verifying identity and resetting a password.

## Steps
1. Verify user identity
2. Reset or unlock account
3. Confirm MFA path if needed
4. Ask user to test login
5. Document outcome
"@ | Set-Content -Path (Join-Path $root "docs\password-reset-runbook.md")

@"
# Role Access Matrix

| Role | Core Access | Extra Notes |
|---|---|---|
| Finance Analyst | Email, finance share, ERP | Standard business user |
| HR Coordinator | Email, HRIS, HR share | Sensitive data access |
| Engineering Lab User | Email, engineering share, approved software | May need device-specific tools |
"@ | Set-Content -Path (Join-Path $root "docs\role-access-matrix.md")

Write-Host "Project scaffold created at: $root"