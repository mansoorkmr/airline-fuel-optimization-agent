"""
Domain models for operational constraints.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AltitudeConstraint:
    constraint_id: str
    sector: str
    min_altitude_ft: Optional[int]
    max_altitude_ft: Optional[int]
    reason_code: str
    description: str
