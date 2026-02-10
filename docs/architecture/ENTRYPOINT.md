# System Entry Point – Architecture

## Purpose
The system entry point wires together all layers and executes the
fuel optimization pipeline in a deterministic sequence.

## Execution Flow
1. Load configuration
2. Load ingestion data
3. Initialize services
4. Run optimization workflow
5. Generate MCP message
6. Generate audit report
7. Persist outputs

## Design Principles
- No business logic
- Explicit dependency wiring
- Single execution path
- HPC and cloud compatible

## Non-Responsibilities
- No optimization logic
- No transport logic
- No parallelization
