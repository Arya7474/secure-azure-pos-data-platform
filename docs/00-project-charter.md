# Project Charter

## Project Name
Secure Azure POS Data Platform

## Problem Statement
As a Data Engineer, I want to build a secure Azure-based data platform that ingests daily POS sales data, transforms it, and loads it into a dimensional warehouse.

The main focus of this project is not complex business logic. The main focus is:

- using multiple Azure data services together
- designing enterprise-style architecture
- deploying securely
- keeping services private where possible
- preparing the solution for CI/CD

## Business Goal
Build a simple POS analytics pipeline that demonstrates how Azure services are used together in a secure enterprise environment.

## Services in Scope
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- Azure Logic App Standard
- Azure SQL Database
- Azure Synapse Dedicated SQL Pool
- Azure Key Vault
- Log Analytics
- Azure DevOps

## High-Level Data Flow
1. POS sales and master data files land in ADLS Gen2.
2. Azure Data Factory orchestrates the pipeline.
3. Databricks reads and transforms the files.
4. Curated/stage outputs are written back to ADLS.
5. Synapse Dedicated SQL Pool stores the dimensional warehouse.
6. Azure SQL DB stores control tables, watermark, and audit logs.
7. Logic App sends notifications for success/failure events.

## Security Goal
The platform should be designed with enterprise security patterns such as:

- private endpoints
- private DNS
- managed identity
- Key Vault-based secret management
- no unnecessary public exposure
- CI/CD driven deployments

## Final Warehouse Model
- DimDate
- DimStore
- DimProduct
- FactSales

## Environment Strategy
For now, this project will use only one development resource group due to cost limitations.
