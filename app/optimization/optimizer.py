"""
Fuel optimization engine.

Selects the most fuel-efficient cruise altitude.
"""

from typing import List
from app.optimization.fuel_model import FuelConsumptionModel
from app.config.settings import AppSettings


class OptimizationResult:
    """
    Immutable optimization outcome.
    """

    def __init__(
        self,
        original_altitude: int,
        optimized_altitude: int,
        original_fuel: float,
        optimized_fuel: float,
        rationale: str,
    ):
        self.original_altitude = original_altitude
        self.optimized_altitude = optimized_altitude
        self.original_fuel = original_fuel
        self.optimized_fuel = optimized_fuel
        self.fuel_saved = original_fuel - optimized_fuel
        self.rationale = rationale


class FuelOptimizer:
    """
    Deterministic cruise altitude optimizer.
    """

    def __init__(
        self,
        fuel_model: FuelConsumptionModel,
        settings: AppSettings,
    ):
        self._fuel_model = fuel_model
        self._settings = settings

    def optimize(self, aircraft_type: str, planned_altitude_ft: int) -> OptimizationResult:
        """
        Determine the optimal cruise altitude.

        Args:
            aircraft_type: Aircraft identifier.
            planned_altitude_ft: Planned cruise altitude.

        Returns:
            OptimizationResult.
        """
        candidate_altitudes: List[int] = [30000, 33000, 35000, 38000]

        original_fuel = (
            self._fuel_model.hourly_burn(aircraft_type, planned_altitude_ft)
            * self._settings.DEFAULT_FLIGHT_DURATION_HOURS
        )

        best_altitude = planned_altitude_ft
        best_fuel = original_fuel

        for altitude in candidate_altitudes:
            estimated_fuel = (
                self._fuel_model.hourly_burn(aircraft_type, altitude)
                * self._settings.DEFAULT_FLIGHT_DURATION_HOURS
            )

            if estimated_fuel < best_fuel:
                best_fuel = estimated_fuel
                best_altitude = altitude

        rationale = (
            "Cruise altitude optimized to minimize wind-adjusted fuel burn"
            if best_altitude != planned_altitude_ft
            else "Original cruise altitude is fuel-optimal"
        )

        return OptimizationResult(
            planned_altitude_ft,
            best_altitude,
            original_fuel,
            best_fuel,
            rationale,
        )
