# ADR-002: Operational Constraint Engine

## Status
Accepted

## Context
Fuel-optimal plans may violate ATC or airline constraints.

## Decision
Introduce a dedicated ConstraintService that validates
optimized plans before MCP publication.

## Consequences
- Legal safety guaranteed
- Optimizer purity preserved
- Enables future ATC integrations
