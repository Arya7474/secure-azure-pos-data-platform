# Security Design

The platform follows modern Azure security best practices.

## Identity Strategy

Managed Identity will be used wherever possible.

Services using Managed Identity:

Azure Data Factory
Azure Databricks
Azure Logic App

These identities will receive RBAC permissions on required resources.

## Secret Management

Secrets such as:

database connection strings
API keys
service credentials

will be stored in Azure Key Vault.

Services will reference secrets using Key Vault integration.

## RBAC Model

Storage Account

ADF → Storage Blob Data Contributor
Databricks → Storage Blob Data Contributor

Key Vault

ADF → Key Vault Secrets User
Databricks → Key Vault Secrets User

Synapse

Databricks → SQL permissions
ADF → pipeline orchestration only

## Network Security

Services will communicate through:

Private Endpoints
VNet integration

Minimizing public exposure.

