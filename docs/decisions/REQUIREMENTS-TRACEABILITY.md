# Requirements Traceability Matrix
Airline Fuel Optimization Agent (AWS Strands & MCP)

## Purpose
This document provides a formal traceability mapping between the
coding challenge requirements and the implemented system artifacts.

It is intended to demonstrate completeness, architectural rigor,
and auditability of the solution.

---

## 1. Data Ingestion

### Requirement
Connect to sample flight data (CSV, API, or mock data).

### Implementation
- Module: `app/ingestion/flight_repository.py`
- Mechanism: CSV-based ingestion
- Data Source: `data/flights.csv`

### Evidence
- Successful ingestion verified in Phase 7
- Domain objects instantiated deterministically
- Output artifacts generated per flight

### Scope Notes
- CSV chosen as authoritative POC input
- API integration intentionally deferred for extensibility

---

### Requirement
Fetch METAR/TAF weather reports for flight waypoints.

### Implementation
- Module: `app/services/weather_service.py`
- Mechanism: Mocked weather payload (JSON)
- Data Source: `data/weather.json`

### Evidence
- Wind component applied in fuel model
- Deterministic weather influence verified in optimization outputs

### Scope Notes
- METAR/TAF parsing is abstracted
- Real METAR/TAF integration documented as future extension
- WeatherService API remains stable for real data substitution

---

### Requirement
Simulate or retrieve aircraft performance metrics.

### Implementation
- Module: `app/services/aircraft_service.py`
- Mechanism: Static performance model
- Data Source: `data/aircraft_performance.json`

### Evidence
- Fuel burn rates used in optimization core
- Altitude-dependent fuel consumption verified

---

## 2. Core Logic – Fuel Optimization

### Requirement
Identify optimal routing and altitude adjustments based on weather and operational constraints.

### Implementation
- Module: `app/optimization/optimizer.py`
- Strategy: Vertical (altitude) optimization
- Candidate evaluation: Deterministic altitude set

### Evidence
- Optimized altitude selected (e.g., 35000 → 38000 ft)
- Positive fuel savings observed

### Scope Notes
- Lateral routing intentionally out of scope for POC
- Vertical optimization selected for clarity and determinism

---

### Requirement
Estimate fuel consumption and savings for each proposed route.

### Implementation
- Module: `app/optimization/fuel_model.py`
- Model: Fuel burn + wind penalty × duration

### Evidence
- Original vs optimized fuel explicitly reported
- Fuel savings included in MCP and audit outputs

---

### Requirement
Provide recommendations (route/altitude changes, delay, or re-dispatch).

### Implementation
- Module: `app/mcp/publisher.py`
- Recommendation Logic: CLIMB / MAINTAIN

### Evidence
- MCP decision payload includes recommendation and rationale

### Scope Notes
- Delay and re-dispatch logic deferred
- Recommendation framework designed for extension

---

## 3. AWS Strands & MCP Integration

### Requirement
Deploy logic within an AWS Lambda or containerized app.

### Implementation
- Execution Model: AWS Lambda (container-ready)
- Entry Point: `app/aws/lambda_handler.py`

### Evidence
- Lambda handler maps directly to flight task
- No business logic duplicated

---

### Requirement
Use AWS Strands for orchestrating data analysis and optimization steps.

### Implementation
- Module: `app/workflow/strands_state_machine.py`
- Design: Deterministic workflow abstrac
