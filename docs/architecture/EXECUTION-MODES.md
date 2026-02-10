# Execution Modes

## Local Execution
- Entry: `python -m app.main`
- Purpose: Development & testing

## HPC Execution
- Entry: Slurm job arrays
- One flight per task
- Deterministic, parallel execution

## AWS Execution
- Entry: AWS Lambda
- Orchestrated via Step Functions
- EventBridge used for MCP transport

## Guarantee
All modes execute identical logic.
