# Mission Control Protocol (MCP) – Architecture

## Purpose
The Mission Control Protocol (MCP) defines the authoritative contract
for communicating optimization recommendations to airline operational systems.

## Design Principles
- Contract-first
- Deterministic payloads
- Explicit operational intent
- Audit-friendly structure

## Responsibilities
- Define recommendation semantics
- Provide structured optimization output
- Enable downstream operational decisions

## Non-Responsibilities
- No transport logic (SNS, EventBridge handled later)
- No optimization logic
- No workflow orchestration

## Versioning
MCP messages are versioned and backward-compatible.
