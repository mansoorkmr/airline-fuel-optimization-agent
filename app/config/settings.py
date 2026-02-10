"""
Application-wide configuration.

This module defines immutable configuration parameters used across
the system. These values are version-controlled and auditable.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppSettings:
    """
    Immutable application settings.
    """

    # Default flight duration assumption (hours)
    DEFAULT_FLIGHT_DURATION_HOURS: float = 2.0

    # Fuel penalty per knot of wind (kg/hr)
    WIND_PENALTY_FACTOR: float = 5.0

    # System identity
    SYSTEM_NAME: str = "airline-fuel-optimization-agent"

    # MCP version
    MCP_VERSION: str = "1.0"
