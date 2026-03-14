# Scope and Assumptions

## In Scope
- One Azure development resource group
- One secure data platform design
- Sample POS source files
- ADLS landing, curated, and stage zones
- ADF orchestration
- Databricks transformation notebooks
- Azure SQL DB control tables
- Synapse dedicated SQL pool dimensional model
- Logic App notifications
- Key Vault integration
- CI/CD-ready repository structure

## Out of Scope
- Multi-region deployment
- Production-grade HA/DR
- Real-time streaming ingestion
- Complex SCD Type 2 implementation in first version
- Full enterprise policy automation across subscription
- Multiple environments (dev/uat/prod) in initial release

## Assumptions
- The solution is built for interview and learning purposes.
- Source files are small CSV files.
- One daily batch load is enough.
- Cost should be controlled aggressively.
- Security design should be strong even if scale is small.
