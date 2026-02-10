"""
Aircraft performance service.

Provides access to aircraft fuel burn characteristics.
"""

from typing import Dict


class AircraftService:
    """
    Read-only aircraft performance lookup service.
    """

    def __init__(self, aircraft_payload: Dict):
        self._aircraft_payload = aircraft_payload

    def fuel_burn(self, aircraft_type: str, altitude_ft: int) -> float:
        """
        Retrieve fuel burn rate (kg/hr) for an aircraft at a given altitude.

        Args:
            aircraft_type: Aircraft identifier (e.g., A320).
            altitude_ft: Cruise altitude in feet.

        Returns:
            Fuel burn rate in kg/hr.
        """
        return float(
            self._aircraft_payload[aircraft_type]["fuel_burn_kg_per_hr"][str(altitude_ft)]
        )
