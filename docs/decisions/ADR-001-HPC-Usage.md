# ADR-001: Use of HPC for Pre-Production Optimization

## Decision
HPC is used for development, simulation, and validation only.

## Rationale
- High compute availability
- Low cost
- Safe isolation from operational systems

## Consequences
- Production deployment remains on AWS
- MCP publishing from HPC is test-only
