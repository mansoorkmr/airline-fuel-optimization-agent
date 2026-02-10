# Workflow Layer – Architecture (Strands-Compatible)

## Purpose
The workflow layer orchestrates the execution of domain, services,
and optimization components in a deterministic sequence.

## Design Principles
- No business logic
- No decision-making
- Deterministic step execution
- Explicit state transitions

## Responsibilities
- Invoke optimization for a single flight
- Maintain execution order
- Provide a clear mapping to AWS Strands / Step Functions

## Non-Responsibilities
- No optimization logic
- No data ingestion
- No MCP publishing
- No parallelization logic

## Strands Mapping
Each method in this layer corresponds to a future Strands state.
