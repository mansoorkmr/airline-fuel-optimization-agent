"""
Audit report generator.

Produces deterministic, human-readable audit records for optimization runs.
"""

from typing import Dict
from app.optimization.optimizer import OptimizationResult


def generate_audit_report(
    flight_id: str,
    result: OptimizationResult,
) -> Dict:
    """
    Generate an audit report for a flight optimization.

    Args:
        flight_id: Flight identifier.
        result: OptimizationResult.

    Returns:
        Dictionary representing audit record.
    """
    return {
        "flight_id": flight_id,
        "original_altitude_ft": result.original_altitude,
        "optimized_altitude_ft": result.optimized_altitude,
        "original_fuel_kg": result.original_fuel,
        "optimized_fuel_kg": result.optimized_fuel,
        "fuel_saved_kg": result.fuel_saved,
        "decision_rationale": result.rationale,
    }
