# Optimization Scope & Limits

## Purpose
Define the precise optimization scope implemented in the POC.

## Implemented Optimization
- Vertical optimization (cruise altitude selection)
- Deterministic candidate evaluation
- Wind-adjusted fuel consumption

## Optimization Strategy
- Fixed candidate altitude set
- Objective: minimize fuel burn
- Deterministic selection

## Explicit Non-Scope
- Lateral routing optimization
- Airspace network graphs
- ATC slot constraints
- Delay modeling
- Re-dispatch logic

## Rationale
Vertical optimization was selected to:
- Demonstrate optimization clarity
- Preserve explainability
- Avoid unnecessary complexity

The architecture supports future expansion.

