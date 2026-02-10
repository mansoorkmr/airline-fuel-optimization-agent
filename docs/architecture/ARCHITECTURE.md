# Airline Fuel Optimization Agent – Architecture

## Architectural Principles
- Stateless compute
- Deterministic optimization
- Stateful orchestration via AWS Strands
- Contract-first MCP integration
- Separation of concerns

## Layers
1. Domain Layer
2. Ingestion Layer
3. Services Layer
4. Optimization Layer
5. Workflow (Strands) Layer
6. MCP Integration Layer
7. Reporting & Audit Layer

## Execution Contexts
- HPC: Development, simulation, stress testing
- AWS: Production orchestration and MCP delivery

## Non-Goals
- HPC is not production
- No direct airline ops integration from HPC
