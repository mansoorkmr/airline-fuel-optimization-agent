✈️ Airline Fuel Optimization Agent
AWS Strands–Aligned | MCP-Integrated | Operationally Safe | Shadow-Tested

Author: Mansoor Wani

Email: mansoor.wani@iust.ac.in

GitHub: https://github.com/mansoorkmr

📄 Executive Summary
This project implements an institutional-grade Proof-of-Concept Airline Fuel Optimization Agent.

The system analyzes:

Flight plan data

Weather signals

Aircraft performance models

Operational airspace constraints

It produces:

Legally compliant cruise altitude optimization

Fuel savings estimation (kg and %)

MCP-compliant operational recommendations

Fleet-level cost and annualized financial projections

Shadow-mode backtesting analysis

Note: This architecture is aligned with AWS Strands-style orchestration and MCP event-driven integration.

❓ Problem Statement
Airline fuel represents the largest operational cost component. Small improvements in cruise altitude selection can generate significant fleet-wide savings.

However, optimization must respect:

Weather conditions

Aircraft performance limits

ATC operational constraints

Legal airspace restrictions

Dispatch governance

The challenge: To build a deterministic, auditable, operationally safe optimization agent.

🏗️ System Architecture
Full Diagram: docs/architecture/ARCHITECTURE-DIAGRAM.md

High-level Flow
Flight Data → Optimization Workflow (Strands-style orchestration) → Fuel Model + Constraints → MCP Recommendation → Shadow Analytics → Fleet Financial Summary

Core Architectural Layers
Domain Layer: Immutable flight models

Ingestion Layer: CSV abstraction

Services Layer: Weather + aircraft

Constraint Engine: ATC legality

Optimization Engine: Deterministic

Workflow Orchestrator: Strands abstraction

MCP Publisher: Structured event emission

Shadow Analyzer: Backtesting & fleet projection

No business logic is embedded in AWS SDK calls. Core logic is platform-agnostic.

🛠️ Core Capabilities
4.1 Data Ingestion
Flight plan ingestion from CSV

Weather abstraction layer

Aircraft performance modeling

Config-driven file paths

Future extension: Real METAR/TAF API ingestion (NOAA/AVWX)

4.2 Deterministic Fuel Optimization
The optimizer uses config-driven candidate altitudes, applies wind penalty factors, computes fuel burn per altitude, selects the minimum fuel option, and enforces operational legality.

Optimization Characteristics:

Deterministic & Auditable

Stateless & Reproducible

4.3 Operational Constraint Engine
Implements legality validation including restricted airspace ingestion and ATC LOA altitude prohibitions via segment-based enforcement.

Logic: If fuel-optimal altitude violates legality, the optimization is rejected, the rationale is recorded, and the MCP reflects the constraint rejection.

Outcome: Ensures operational compliance.

4.4 Shadow Mode (Backtesting Engine)
Shadow mode enables production-safe validation by replaying historical flight plans to compute “Recommended vs Actual” metrics.

Outputs:

Total fuel saved (kg & %)

Projected annual fuel savings

USD cost savings

Fleet-level impact summary

4.5 MCP Integration
Outputs MCP-compliant event structure:

JSON
{ 
  "event_type": "AIRLINE_FUEL_OPTIMIZATION_RECOMMENDATION", 
  "impact": { 
    "fuel_saved_kg": 320, 
    "fuel_saved_percent": 4.17 
  } 
}
Designed for: Mission Control ingestion, EventBridge topic publishing, and Queue-based operational workflows.

Status: Currently broadcast-only. Bi-directional ACK/NACK loop planned.

☁️ AWS Strands Alignment
Although implemented locally, the architecture maps directly to:

AWS Lambda: Stateless compute

AWS Step Functions: State orchestration

EventBridge: MCP emission

S3: Audit storage

CloudWatch: Observability

Workflow abstraction: app/workflow/strands_state_machine.py. No AWS SDK hardcoded inside business logic.

⚙️ Configuration & Financials
Configuration Abstraction
All runtime behavior is externalized to config.ini. No hardcoded business constants.

Sections: optimization, weather, fleet, execution, logging, paths.

Fleet Financial Modeling
Moves the system from technical demo to executive-relevant solution.

Metrics: Fuel saved per flight, Cost per kg, Flights per day, Operating days per year.

Example Calculation: > 320 kg per flight × 100 flights/day × 365 days × 0.85 USD/kg → Significant annual cost reduction.

🧪 Quality & Execution
Testing & Engineering Quality
Unit tests for optimizer logic

Deterministic behavior & constraint validation tested

CI-ready structure with layered architecture and no hidden state

Test example: tests/test_optimizer.py | Run: pytest

Execution Modes
Configured via config.ini. Modes: local, shadow.

Run command: python -m app.main

Outputs: Flight-level MCP JSON, Audit JSON, Fleet summary JSON.

🚀 Future Roadmap
Production Readiness Considerations
Replace mock weather with live METAR/TAF ingestion

Introduce MCP ACK/NACK loop

Add real-time dispatcher UI

Implement cost index modeling

Add CI/CD deployment & Containerization (Docker)

Extensibility Roadmap
Real-time NOAA weather API

Machine-learning fuel modeling

Dynamic re-dispatch engine

Turbulence-aware altitude modeling

Multi-aircraft fleet optimization

📁 Repository Structure
Plaintext
app/
├── core/ (domain, ingestion, services)
├── constraints/
├── optimization/
├── workflow/
├── mcp/
├── shadow/
└── reporting/
docs/ (architecture, decisions, runbooks)
tests/
config.ini
🏁 Conclusion
This project demonstrates engineering discipline, operational safety awareness, and financial impact modeling. It exceeds baseline POC requirements by introducing:

Constraint enforcement

Shadow-mode validation

Fleet-level financial analytics

Deterministic optimization logic
