"""
HPC flight-level execution entry point.

Executes optimization for a single flight.
"""

import json
import sys
from pathlib import Path

from app.config.settings import AppSettings
from app.ingestion.flight_repository import FlightRepository
from app.services.weather_service import WeatherService
from app.services.aircraft_service import AircraftService
from app.optimization.fuel_model import FuelConsumptionModel
from app.optimization.optimizer import FuelOptimizer
from app.workflow.strands_state_machine import FuelOptimizationWorkflow
from app.mcp.publisher import MCPPublisher
from app.reporting.audit_report import generate_audit_report


def main(flight_index: int) -> None:
    data_dir = Path("data")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    settings = AppSettings()

    flights = FlightRepository.load_from_csv(data_dir / "flights.csv")
    flight = flights[flight_index]

    weather = WeatherService(json.load(open(data_dir / "weather.json")))
    aircraft = AircraftService(json.load(open(data_dir / "aircraft_performance.json")))

    fuel_model = FuelConsumptionModel(aircraft, weather, settings)
    optimizer = FuelOptimizer(fuel_model, settings)
    workflow = FuelOptimizationWorkflow(optimizer)
    publisher = MCPPublisher(settings)

    result = workflow.run(flight)

    mcp_message = publisher.publish(flight.flight_id, result)
    audit_report = generate_audit_report(flight.flight_id, result)

    with open(output_dir / f"{flight.flight_id}_mcp.json", "w") as f:
        json.dump(mcp_message, f, indent=2)

    with open(output_dir / f"{flight.flight_id}_audit.json", "w") as f:
        json.dump(audit_report, f, indent=2)


if __name__ == "__main__":
    index = int(sys.argv[1])
    main(index)
