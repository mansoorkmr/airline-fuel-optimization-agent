"""
Aircraft performance domain entity.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class AircraftPerformance:
    """
    Immutable aircraft performance characteristics.
    """

    aircraft_type: str
    fuel_burn_kg_per_hr: Dict[int, float]
