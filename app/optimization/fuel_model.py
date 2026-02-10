"""
Fuel consumption model.

Provides deterministic fuel burn estimation.
"""

from app.services.aircraft_service import AircraftService
from app.services.weather_service import WeatherService
from app.config.settings import AppSettings


class FuelConsumptionModel:
    """
    Deterministic fuel consumption estimator.
    """

    def __init__(
        self,
        aircraft_service: AircraftService,
        weather_service: WeatherService,
        settings: AppSettings,
    ):
        self._aircraft_service = aircraft_service
        self._weather_service = weather_service
        self._settings = settings

    def hourly_burn(self, aircraft_type: str, altitude_ft: int) -> float:
        """
        Estimate hourly fuel burn adjusted for wind.

        Args:
            aircraft_type: Aircraft identifier.
            altitude_ft: Cruise altitude in feet.

        Returns:
            Estimated fuel burn in kg/hr.
        """
        base_burn = self._aircraft_service.fuel_burn(aircraft_type, altitude_ft)
        wind_penalty = abs(
            self._weather_service.wind_component("ENROUTE")
        ) * self._settings.WIND_PENALTY_FACTOR
        return base_burn + wind_penalty
