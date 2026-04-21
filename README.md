# IT Operations Support Hub

A lightweight internal IT support portal MVP built with **Python + Streamlit**, designed to simulate real-world IT operations workflows and evolve into a **homelab-integrated incident management system**.

## Overview

This project started as a simple internal IT support portal for managing:

- service requests
- incident tracking
- knowledge base articles
- account and access workflows

The long-term goal is to expand it into a **mini enterprise IT environment** connected to my homelab, where monitoring events can automatically generate incident records, link to troubleshooting documentation, and support operational workflows.

## Why I Built This

I wanted a project that demonstrates more than just coding. This repo is meant to show:

- IT support workflow thinking
- infrastructure awareness
- documentation and process design
- incident and request handling
- modular automation
- a bridge between homelab operations and internal IT tooling

Instead of building disconnected demos, this project is meant to become a central **IT operations hub**.

## Current Features

- Streamlit-based multi-page internal portal
- Request / incident tracking
- Knowledge base view
- Service catalog
- Account and access workflow pages
- Asset-oriented structure
- CSV-backed MVP data model for fast iteration

## Planned Direction

This project is being expanded toward a more realistic IT ops workflow, including:

- service monitoring
- incident auto-creation from failed checks
- asset-linked incident records
- knowledge base recommendations
- remediation tracking
- optional homelab integration with CasaOS-hosted services

## Tech Stack

- Python
- Streamlit
- Pandas
- PowerShell
- CSV data storage

Planned future additions may include:

- SQLite
- Docker / CasaOS integration
- uptime monitoring
- log-based incident triggers
- optional local AI-assisted incident summaries

## Repository Structure

```text
IT-Operations-Support-Hub/
├── .streamlit/              # Streamlit config
├── data/                    # CSV-backed MVP data
├── docs/                    # Supporting project docs
├── pages/                   # Streamlit multipage views
├── utils/                   # Helper scripts / future monitoring logic
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── seed-data.ps1            # Seed local sample data
├── setup-project.ps1        # Project setup helper
├── start-dev.ps1            # Local development launcher
└── README.md
```

## Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/N3onKashimo/IT-Operations-Support-Hub.git
cd IT-Operations-Support-Hub
```

### 2. Create and activate a virtual environment

#### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

## Current Data Model

The MVP currently uses CSV files in the `data/` directory for fast iteration and visibility.

Examples include:

- `requests.csv`
- `kb_articles.csv`
- `service_catalog.csv`

This will likely evolve into SQLite once the incident workflow becomes more dynamic.

## Roadmap

### Near-term
- Improve request and incident schema
- Add better dashboard filtering
- Seed more realistic services, assets, and KB articles
- Build one real end-to-end workflow:
  - monitor service
  - detect failure
  - create incident
  - display in dashboard

### Mid-term
- Connect to homelab / CasaOS services
- Add monitor scripts under `utils/`
- Move from static demo data to generated incidents
- Add remediation notes and incident lifecycle statuses

### Long-term
- Convert into a mini internal IT department simulation
- Integrate monitoring, asset view, KB, and incident workflows
- Optionally add local AI for summarizing incidents and recommending next steps

## Example Use Case

A future intended flow for this project:

1. A monitored service in my homelab fails
2. A script detects the failure
3. An incident record is created automatically
4. The dashboard shows the affected service and asset
5. A related knowledge base article is suggested
6. The issue can be tracked through investigation and resolution

## Project Goal

This repo is not just meant to be a dashboard.

It is being built as a practical portfolio project that demonstrates:

- IT support operations
- service lifecycle awareness
- internal tooling design
- process documentation
- homelab-to-operations integration

## Notes

This is an actively evolving MVP. The current version focuses on structure and workflow clarity first, with deeper automation being added incrementally.

## Author

Built by [N3onKashimo](https://github.com/N3onKashimo)