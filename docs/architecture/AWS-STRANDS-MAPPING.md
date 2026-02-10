# AWS Strands / Step Functions Mapping

## Execution Model
- One flight per Lambda invocation
- Step Functions Map state for batch flights

## State Machine
1. Load flight list
2. Map over flights
3. Invoke optimization task
4. Publish MCP message
5. Persist audit output

## Determinism
- Stateless Lambdas
- Idempotent execution
- Replay-safe

## Failure Handling
- Per-flight retries
- Dead-letter queue for MCP failures
