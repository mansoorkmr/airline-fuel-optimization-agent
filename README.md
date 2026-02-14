# ✈️ Airline Fuel Optimization Agent  
### AWS Strands–Aligned | MCP-Integrated | Operationally Safe | Shadow-Tested  

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Strands%20Aligned-orange)
![Integration](https://img.shields.io/badge/MCP-Integrated-purple)
![Mode](https://img.shields.io/badge/Execution-Shadow%20Tested-green)
![Design](https://img.shields.io/badge/Design-Deterministic-critical)

</p>

---

## 👤 Author

**Mansoor Wani**  
📧 mansoor.wani@iust.ac.in  
🔗 https://github.com/mansoorkmr  

---

# 📌 Executive Summary

This project implements an institutional-grade Proof-of-Concept Airline Fuel Optimization Agent.

The system analyzes:

- Flight plan data  
- Weather signals  
- Aircraft performance models  
- Operational airspace constraints  

It produces:

- Legally compliant cruise altitude optimization  
- Fuel savings estimation (kg and %)  
- MCP-compliant operational recommendations  
- Fleet-level cost and annualized financial projections  
- Shadow-mode backtesting analysis  

This architecture is aligned with AWS Strands-style orchestration and MCP event-driven integration.

---

# 🎯 Problem Statement

Airline fuel represents the largest operational cost component. Small improvements in cruise altitude selection can generate significant fleet-wide savings.

However, optimization must respect:

- Weather conditions  
- Aircraft performance limits  
- ATC operational constraints  
- Legal airspace restrictions  
- Dispatch governance  

The challenge is to build a deterministic, auditable, operationally safe optimization agent.

---

# 🏗 System Architecture

Full diagram:  
`docs/architecture/ARCHITECTURE-DIAGRAM.md`

## 🔄 High-Level Flow

```
Flight Data
      ↓
Optimization Workflow (Strands-style orchestration)
      ↓
Fuel Model + Constraints
      ↓
MCP Recommendation
      ↓
Shadow Analytics
      ↓
Fleet Financial Summary
```

---

## 🧱 Core Architectural Layers

- Domain Layer (immutable flight models)  
- Ingestion Layer (CSV abstraction)  
- Services Layer (weather + aircraft)  
- Constraint Engine (ATC legality)  
- Optimization Engine (deterministic)  
- Workflow Orchestrator (Strands abstraction)  
- MCP Publisher (structured event emission)  
- Shadow Analyzer (backtesting & fleet projection)  

No business logic is embedded in AWS SDK calls. Core logic is platform-agnostic.

---

# 🚀 Core Capabilities

---

## 4.1 Data Ingestion

- Flight plan ingestion from CSV  
- Weather abstraction layer  
- Aircraft performance modeling  
- Config-driven file paths  

Future extension: Real METAR/TAF API ingestion (NOAA/AVWX)

---

## 4.2 Deterministic Fuel Optimization

The optimizer:

- Uses config-driven candidate altitudes  
- Applies wind penalty factor  
- Computes fuel burn per altitude  
- Selects minimum fuel option  
- Enforces operational legality  

Optimization is:

- Deterministic  
- Auditable  
- Stateless  
- Reproducible  

---

## 4.3 Operational Constraint Engine

Implements legality validation:

- Restricted airspace ingestion  
- ATC LOA altitude prohibitions  
- Segment-based enforcement  

If fuel-optimal altitude violates legality:

- Optimization is rejected  
- Rationale is recorded  
- MCP reflects constraint rejection  

This ensures operational compliance.

---

## 4.4 Shadow Mode (Backtesting Engine)

Shadow mode enables production-safe validation:

- Replays historical flight plans  
- Computes “Recommended vs Actual”  
- Measures fuel delta  
- Aggregates fleet impact  

Outputs:

- Total fuel saved  
- Percentage savings  
- Projected annual fuel savings  
- USD cost savings  
- Fleet-level impact summary  

Shadow mode allows validation before operational deployment.

---

## 4.5 MCP Integration

Outputs MCP-compliant event structure:

```json
{
  "event_type": "AIRLINE_FUEL_OPTIMIZATION_RECOMMENDATION",
  "impact": {
    "fuel_saved_kg": 320,
    "fuel_saved_percent": 4.17
  }
}
```

Designed for:

- Mission Control ingestion  
- EventBridge topic publishing  
- Queue-based operational workflows  

Currently broadcast-only. Bi-directional ACK/NACK loop planned.

---

# ☁️ AWS Strands Alignment

Although implemented locally, architecture maps directly to:

- AWS Lambda (stateless compute)  
- AWS Step Functions (state orchestration)  
- EventBridge (MCP emission)  
- S3 (audit storage)  
- CloudWatch (observability)  

Workflow abstraction in:

`app/workflow/strands_state_machine.py`

No AWS SDK hardcoded inside business logic.

---

# ⚙️ Configuration Abstraction

All runtime behavior externalized to:

`config.ini`

Sections:

- optimization  
- weather  
- fleet  
- execution  
- logging  
- paths  

No hardcoded business constants.

---

# 💰 Fleet Financial Modeling

Fleet metrics include:

- Fuel saved per flight  
- Cost per kg  
- Flights per day  
- Operating days per year  
- Annualized savings  

Example:

```
320 kg per flight × 100 flights/day × 365 days × 0.85 USD/kg
→ Significant annual cost reduction
```

This moves the system from technical demo to executive-relevant solution.

---

# 🧪 Testing & Engineering Quality

- Unit tests for optimizer logic  
- Deterministic behavior  
- Config-driven candidate altitudes  
- Constraint validation tested  
- CI-ready structure  
- Layered architecture  
- No hidden state  

Test example:

`tests/test_optimizer.py`

Run:

```
pytest
```

---

# ▶️ Execution Modes

Configured via `config.ini`

Modes:

- local  
- shadow  

Shadow mode enables fleet-level projection.

Run:

```
python -m app.main
```

Outputs:

- Flight-level MCP JSON  
- Audit JSON  
- Fleet summary JSON  

---

# 🏭 Production Readiness Considerations

To move to production:

- Replace mock weather with live METAR/TAF ingestion  
- Introduce MCP ACK/NACK loop  
- Add real-time dispatcher UI  
- Implement cost index modeling  
- Add CI/CD deployment  
- Add containerization (Docker)  

---

# ⚠️ Limitations

- Weather currently simulated  
- No lateral route optimization  
- No real-time ATC integration  
- No ML predictive burn model  

Documented intentionally for clarity.

---

# 🔮 Extensibility Roadmap

Future enhancements:

- Real-time NOAA weather API  
- Machine-learning fuel modeling  
- Dynamic re-dispatch engine  
- Turbulence-aware altitude modeling  
- Real-time dispatch dashboard  
- Multi-aircraft fleet optimization  

---

# 📁 Repository Structure

```
app/
core/
domain/
ingestion/
services/
constraints/
optimization/
workflow/
mcp/
shadow/
reporting/
docs/
architecture/
decisions/
runbooks/
tests/
config.ini
```

---

# 🏁 Conclusion

This project demonstrates:

- Engineering discipline  
- Operational safety awareness  
- Financial impact modeling  
- AWS-aligned architecture  
- Deterministic optimization logic  
- Enterprise-ready modular design  

It exceeds baseline POC requirements by introducing:

- Constraint enforcement  
- Shadow-mode validation  
- Fleet-level financial analytics  
- Config abstraction  
- CI-ready structure  

---

<p align="center">
<strong>Institutional-grade optimization logic with operational safety and executive visibility.</strong>
</p>

