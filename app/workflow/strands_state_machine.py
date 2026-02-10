"""
Workflow state machine.

This module defines a Strands-compatible workflow abstraction.
"""

from app.domain.flight import Flight
from app.optimization.optimizer import FuelOptimizer, OptimizationResult


class FuelOptimizationWorkflow:
    """
    Deterministic workflow for optimizing a single flight.
    """

    def __init__(self, optimizer: FuelOptimizer):
        self._optimizer = optimizer

    def run(self, flight: Flight) -> OptimizationResult:
        """
        Execute the optimization workflow for a flight.

        Args:
            flight: Flight domain object.

        Returns:
            OptimizationResult.
        """
        return self._optimizer.optimize(
            aircraft_type=flight.aircraft_type,
            planned_altitude_ft=flight.cruise_altitude_ft,
        )
