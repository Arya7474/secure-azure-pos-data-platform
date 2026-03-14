# Service Connectivity

## Data Ingestion

Azure Data Factory reads files from ADLS landing container.

## Transformation

ADF triggers Databricks notebook jobs.

Databricks reads landing files from ADLS.

Databricks writes curated datasets to ADLS.

## Warehouse Load

ADF triggers warehouse load process.

Curated datasets are copied into Synapse Dedicated SQL Pool.

## Control Tables

Azure SQL Database stores:

pipeline audit logs
watermark values
load history

## Notification Flow

Logic App is triggered on pipeline success or failure.

Notifications can be sent through email or Teams.
