"""
Weather service.

Provides access to weather data relevant for fuel optimization.
"""

from typing import Dict


class WeatherService:
    """
    Read-only weather lookup service.
    """

    def __init__(self, weather_payload: Dict):
        self._weather_payload = weather_payload

    def wind_component(self, location: str) -> int:
        """
        Retrieve wind component (knots) for a given location.

        Args:
            location: Logical waypoint or ICAO identifier.

        Returns:
            Wind component in knots. Defaults to 0 if unavailable.
        """
        return int(self._weather_payload.get(location, {}).get("wind_kt", 0))
