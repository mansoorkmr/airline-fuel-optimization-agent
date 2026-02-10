# Services Layer – Architecture

## Purpose
The services layer provides access to external or reference data
required by the optimization engine.

## Responsibilities
- Encapsulate access to weather data
- Encapsulate access to aircraft performance data
- Provide simple, deterministic lookup functions

## Non-Responsibilities
- No optimization logic
- No decision-making
- No workflow orchestration
- No persistence

## Current Implementations
- WeatherService (JSON-backed)
- AircraftService (JSON-backed)

## Future Extensions
- Real-time METAR/TAF APIs
- Aircraft manufacturer performance databases
