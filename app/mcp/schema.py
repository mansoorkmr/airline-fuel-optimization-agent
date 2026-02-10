"""
Mission Control Protocol (MCP) schema definition.
"""

def mcp_schema() -> dict:
    """
    Returns the authoritative MCP schema definition.

    This schema defines required fields for operational compliance.
    """
    return {
        "required_fields": [
            "mcp_version",
            "event_type",
            "event_id",
            "timestamp_utc",
            "source_system",
            "flight",
            "original_plan",
            "optimized_plan",
            "impact",
            "decision",
        ]
    }
