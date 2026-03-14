# Network Design

The platform will use a Virtual Network to control service connectivity.

## Virtual Network

vnet-sz-pos-dev

## Subnets

databricks-subnet
Used by Azure Databricks workspace

private-endpoint-subnet
Used by Private Endpoints for services

integration-subnet
Used for integration services if required

## Private Endpoint Services

Private endpoints will be created for:

ADLS Gen2
Azure SQL Database
Azure Synapse
Azure Key Vault

## Public Access Policy

Public access will be disabled for:

ADLS
Key Vault
SQL Database
Synapse

Access will occur through private endpoints where possible.

## Private DNS

Private DNS zones will be used to resolve private endpoint addresses.
