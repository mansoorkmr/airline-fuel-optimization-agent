"""
Mission Control Protocol (MCP) publisher.

Produces MCP-compliant recommendation payloads.
"""

import uuid
from datetime import datetime
from app.config.settings import AppSettings
from app.optimization.optimizer import OptimizationResult


class MCPPublisher:
    """
    Deterministic MCP message builder.
    """

    def __init__(self, settings: AppSettings):
        self._settings = settings

    def publish(self, flight_id: str, result: OptimizationResult) -> dict:
        """
        Build an MCP-compliant recommendation message.

        Args:
            flight_id: Flight identifier.
            result: OptimizationResult.

        Returns:
            MCP message payload as dictionary.
        """
        return {
            "mcp_version": self._settings.MCP_VERSION,
            "event_type": "AIRLINE_FUEL_OPTIMIZATION_RECOMMENDATION",
            "event_id": str(uuid.uuid4()),
            "timestamp_utc": datetime.utcnow().isoformat(),
            "source_system": self._settings.SYSTEM_NAME,
            "flight": {
                "flight_id": flight_id
            },
            "original_plan": {
                "cruise_altitude_ft": result.original_altitude,
                "fuel_kg": result.original_fuel,
            },
            "optimized_plan": {
                "cruise_altitude_ft": result.optimized_altitude,
                "fuel_kg": result.optimized_fuel,
            },
            "impact": {
                "fuel_saved_kg": result.fuel_saved,
            },
            "decision": {
                "recommendation": (
                    "CLIMB"
                    if result.optimized_altitude > result.original_altitude
                    else "MAINTAIN"
                ),
                "confidence": "HIGH",
                "rationale": result.rationale,
            },
        }
