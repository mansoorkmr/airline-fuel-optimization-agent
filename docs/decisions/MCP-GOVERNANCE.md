# MCP Governance & Versioning

## Purpose
Define governance rules for Mission Control Protocol (MCP) messages.

## Versioning
- MCP messages are versioned via `mcp_version`
- Minor changes must be backward-compatible
- Breaking changes require version increment

## Stability Rules
- Required fields cannot be removed
- Semantic meaning must not change silently
- Consumers must handle older versions

## Auditability
Each MCP message is:
- Deterministic
- Timestamped
- Source-identified

This ensures operational trust.
