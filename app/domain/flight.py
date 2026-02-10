"""
Flight domain entity.

This module defines the immutable representation of a flight plan
as provided by airline operational systems.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Flight:
    """
    Immutable flight plan representation.
    """

    flight_id: str
    origin: str
    destination: str
    cruise_altitude_ft: int
    aircraft_type: str
    departure_time_utc: str
