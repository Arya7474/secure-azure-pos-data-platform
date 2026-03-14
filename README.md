# Secure Azure POS Data Platform

## Overview
This project is a hands-on Azure Data Engineering portfolio project focused on building a secure, enterprise-style POS data platform using Azure services.

Main services used:

- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- Azure Logic App Standard
- Azure SQL Database
- Azure Synapse Dedicated SQL Pool
- Azure Key Vault
- Log Analytics
- Azure DevOps

## Project Goal

The goal is to build a simple POS pipeline while focusing heavily on:

- enterprise architecture
- secure networking
- private endpoints
- managed identity
- service-to-service access
- CI/CD readiness

## Final Output

Dimensional warehouse containing:

- DimDate
- DimStore
- DimProduct
- FactSales

## High Level Data Flow

POS Files  
→ ADLS Landing  
→ ADF Orchestration  
→ Databricks Transform  
→ ADLS Curated  
→ Synapse Dedicated SQL Pool

Supporting services:

- Azure SQL DB (control tables)
- Key Vault (secrets)
- Logic App (notifications)
- Log Analytics (monitoring)

## Project Phases

1. Project foundation
2. Source data and dimensional model
3. Architecture and security design
4. Azure resource deployment
5. Identity and access
6. Data lake setup
7. Databricks transformations
8. ADF orchestration
9. Logic App integration
10. Synapse warehouse load
11. CI/CD
12. Monitoring and operations
