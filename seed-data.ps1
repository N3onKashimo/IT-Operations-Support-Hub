Set-Location $PSScriptRoot

Add-Content .\data\assets.csv 'A001,DK-WS-1001,Laptop,jdoe,Finance,Waller,FIN-LT-01,SN123456,Windows 11,In Use,2024-01-15,2027-01-15,Standard user laptop'
Add-Content .\data\assets.csv 'A002,DK-WS-1002,Desktop,asmith,Engineering,Houston,ENG-DT-07,SN223344,Windows 10,In Use,2023-08-10,2026-08-10,Connected to test equipment'

Add-Content .\data\kb_articles.csv 'KB-001,How to Request a New User Account,Accounts & Access,Steps and required info for creating a new employee account,"new hire,onboarding,account,access",Managers,2026-04-18,IT Support,Published,new-user-account'
Add-Content .\data\kb_articles.csv 'KB-002,Password Reset Quick Guide,Accounts & Access,Standard process for resetting a locked or expired password,"password,reset,unlock,mfa",Employees,2026-04-18,IT Support,Published,password-reset'
Add-Content .\data\kb_articles.csv 'KB-003,Printer Troubleshooting Basics,Printing & Peripherals,Common checks for offline or jammed printers,"printer,offline,jam,queue",Employees,2026-04-18,IT Support,Published,printer-troubleshooting'

Add-Content .\data\service_catalog.csv 'SVC-001,New User Account Setup,Accounts & Access,Service Request,Provision baseline account access for a new employee,3,Yes,Manager,KB-001,Active'
Add-Content .\data\service_catalog.csv 'SVC-002,Password Reset / Unlock,Accounts & Access,Service Request,Reset or unlock a user account after identity verification,1,No,,KB-002,Active'
Add-Content .\data\service_catalog.csv 'SVC-003,Printer Support,Printing & Peripherals,Incident,Resolve printer connectivity or print quality issues,2,No,,KB-003,Active'

Add-Content .\data\requests.csv 'R-1001,2026-04-18,Service Request,Accounts & Access,New User Account,Create account for new hire,New hire starting Monday needs laptop login email and VPN,manager1,HR,Waller,,Medium,Open,Service Desk,KB-001,jsantos,2026-04-21,,'
Add-Content .\data\requests.csv 'R-1002,2026-04-18,Incident,Printing & Peripherals,Printer Issue,Printer offline in HR,Shared printer not responding for HR team,hruser,HR,Waller,A001,High,Open,Desktop Support,KB-003,hruser,2026-04-19,,'

Write-Host "Seed data added."