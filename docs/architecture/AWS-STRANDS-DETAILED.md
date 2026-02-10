# AWS Strands Conceptual Mapping

## Definition
AWS Strands represent stateful, deterministic workflows where
each step is explicitly defined and replayable.

## Mapping Strategy
The system implements a Strands-compatible abstraction where:

- Each flight = one strand
- Each optimization = one deterministic execution
- No implicit state exists

## Workflow Mapping
FuelOptimizationWorkflow maps 1:1 to a Step Functions Task state.

## Design Principle
AWS-specific constructs are not embedded in business logic.
This ensures:
- Cloud portability
- Testability
- Clean separation of concerns

## Result
The system can be executed on:
- HPC (Slurm)
- AWS Step Functions
- Local environments

Without code changes.
