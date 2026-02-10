"""
Flight repository.

Responsible for loading flight data from external sources and
producing immutable Flight domain entities.
"""

from typing import List
import pandas as pd
from app.domain.flight import Flight


class FlightRepository:
    """
    Read-only repository for flight plans.
    """

    @staticmethod
    def load_from_csv(csv_path: str) -> List[Flight]:
        """
        Load flight plans from a CSV file.

        Args:
            csv_path: Path to CSV file containing flight plans.

        Returns:
            List of Flight domain objects.
        """
        dataframe = pd.read_csv(csv_path)

        flights: List[Flight] = []

        for _, row in dataframe.iterrows():
            flights.append(
                Flight(
                    flight_id=row["flight_id"],
                    origin=row["origin"],
                    destination=row["destination"],
                    cruise_altitude_ft=int(row["altitude_ft"]),
                    aircraft_type=row["aircraft"],
                    departure_time_utc=row["departure_time"],
                )
            )

        return flights
