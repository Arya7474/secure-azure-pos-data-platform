# Interview Story

## Project Summary
I built a secure Azure POS data platform as a portfolio project to demonstrate not only pipeline development, but also enterprise-grade architecture and deployment practices.

## What makes this project different
Most sample projects focus only on ETL logic. This project focuses on:
- secure architecture
- private networking
- managed identity
- modular infrastructure
- orchestration across multiple Azure services
- final warehouse dimensional modeling

## Business Flow
Daily POS files land in ADLS. ADF orchestrates ingestion and Databricks transformations. Curated outputs are staged back to the lake and loaded into Synapse Dedicated SQL Pool as dimensions and facts. Azure SQL stores control and audit metadata. Logic App handles notifications.

## Security Angle
I designed the platform with private connectivity patterns, Key Vault integration, RBAC, and minimal public exposure.

## Why this matters
This project demonstrates that I can think beyond writing notebooks and pipelines. I can design secure, maintainable, deployable cloud data platforms.
