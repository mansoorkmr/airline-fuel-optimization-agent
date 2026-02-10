# HPC Execution Architecture

## Purpose
Define how the fuel optimization system executes at scale
on HPC infrastructure using Slurm.

## Execution Model
- One flight per Slurm task
- Stateless execution per task
- Deterministic outputs per flight

## Scheduler Strategy
- Slurm job arrays
- CPU-only execution
- Explicit resource requests

## Observability
- Scheduler logs (stdout/stderr)
- Application logs per task
- Output artifacts per flight

## Failure Handling
- Failed tasks can be re-run independently
- No shared mutable state

## Compatibility
- HPC-native
- Cloud batch compatible
