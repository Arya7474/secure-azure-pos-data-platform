# Architecture Decision Log

## ADR-001
### Title
Use one development resource group only

### Decision
Use only one dev resource group for the first version of the platform.

### Reason
This reduces cost and management overhead while still allowing full end-to-end learning.

---

## ADR-002
### Title
Keep business transformation logic simple

### Decision
Use a small POS dataset and a simple dimensional model.

### Reason
The primary goal of the project is secure architecture and service integration, not complex business logic.

---

## ADR-003
### Title
Prefer managed identity over secrets

### Decision
Use managed identities wherever service authentication supports it.

### Reason
This reflects modern enterprise security practices and reduces secret sprawl.

---

## ADR-004
### Title
Use Synapse Dedicated SQL Pool as final warehouse

### Decision
Use dedicated SQL pool as the dimensional warehouse target.

### Reason
This helps demonstrate warehouse loading patterns and interview-ready dimensional modeling.

---

## ADR-005
### Title
Design for privacy-first networking

### Decision
Use private endpoints and private DNS where feasible within cost and service limitations.

### Reason
The platform is intended to showcase enterprise-grade security patterns.
