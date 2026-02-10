"""
Weather domain entity.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Weather:
    """
    Immutable weather representation.
    """

    location: str
    wind_component_kt: int
