# Operational Constraint Engine

## Purpose
Fuel optimization is meaningless if the resulting plan is not
legally or operationally executable.

This layer enforces airline and ATC constraints independently
from fuel optimization logic.

## Constraints Modeled
- ATC Letters of Agreement (LOA)
- Sector altitude restrictions
- Restricted airspace (future)

## Design Principles
- Optimizer remains unaware of constraints
- Workflow enforces legality
- Constraints are data-driven

## Outcome
The system may reject an optimized plan and
fall back to the original flight plan if required.
