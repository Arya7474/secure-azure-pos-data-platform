# Secure Azure POS Data Platform Architecture

```mermaid
flowchart LR

POS[POS Source System]

subgraph Azure_VNet
    subgraph Data_Platform
        ADF[Azure Data Factory]
        DBX[Azure Databricks]
    end

    subgraph Data_Layer
        ADLS_L[ADLS Landing]
        ADLS_C[ADLS Curated]
        SYN[Synapse DWH]
        SQLDB[Control DB]
    end

    subgraph Security
        KV[Key Vault]
        LOG[Log Analytics]
        LA[Logic App]
    end

    subgraph Private_Endpoints
        PE1[Storage PE]
        PE2[SQL PE]
        PE3[Synapse PE]
        PE4[KeyVault PE]
    end
end

POS --> ADLS_L
ADLS_L --> ADF
ADF --> DBX
DBX --> ADLS_C
ADLS_C --> SYN

ADF --> SQLDB
ADF --> KV
DBX --> KV
ADF --> LA
ADF --> LOG
DBX --> LOG
