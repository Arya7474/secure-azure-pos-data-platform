# Architecture Overview

## Objective

Design a secure Azure data platform capable of ingesting POS transaction files,
processing them through a transformation layer, and loading them into a
dimensional warehouse.

The architecture prioritizes:

- secure service communication
- minimal public exposure
- managed identity authentication
- modular service integration

## Core Services

Azure Data Lake Storage Gen2
Azure Data Factory
Azure Databricks
Azure SQL Database
Azure Synapse Dedicated SQL Pool
Azure Key Vault
Azure Logic App Standard
Log Analytics

## High Level Flow

POS CSV Files
→ ADLS Landing Zone
→ Azure Data Factory Orchestration
→ Databricks Transformation
→ ADLS Curated Zone
→ Synapse Dedicated SQL Pool Warehouse

Supporting services:

Azure SQL Database → control tables, audit logging  
Azure Key Vault → secrets and connection references  
Logic App → pipeline notifications  
Log Analytics → monitoring and diagnostics

## Data Zones

Landing

Raw files from source systems

Curated

Transformed datasets produced by Databricks

Warehouse

Dimensional tables stored in Synapse Dedicated SQL Pool
