# Reporting & Audit Layer – Architecture

## Purpose
The reporting and audit layer produces human-readable artifacts
that document optimization decisions and their rationale.

## Design Principles
- Deterministic output
- No side effects beyond file generation
- Read-only consumption of results
- Audit-friendly structure

## Responsibilities
- Generate audit records per flight
- Preserve optimization rationale
- Support post-execution review

## Non-Responsibilities
- No optimization logic
- No MCP publishing
- No workflow orchestration

## Output
- Structured dictionary
- JSON-serializable
- File-based (HPC compatible)
