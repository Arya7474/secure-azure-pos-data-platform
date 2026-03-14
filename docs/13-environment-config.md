# Environment Configuration

This project currently deploys only a development environment due to Azure free-tier limitations.

Future versions can support multiple environments.

## Environments

| Environment | Purpose |
|-------------|--------|
| dev | development and experimentation |
| uat | testing and validation |
| prod | production workloads |

## Current Deployment

| Resource Group | Region |
|----------------|-------|
rg-sz-pos-dev | East US

## Naming Prefix

sz-pos-dev

## Services Deployed

Azure Data Lake Storage Gen2  
Azure Data Factory  
Azure Databricks  
Azure SQL Database  
Azure Synapse Dedicated SQL Pool  
Azure Key Vault  
Azure Logic App  
Log Analytics

## Security Model

Managed Identity for service authentication.

Private Endpoints used for:

Storage  
SQL Database  
Synapse  
Key Vault
