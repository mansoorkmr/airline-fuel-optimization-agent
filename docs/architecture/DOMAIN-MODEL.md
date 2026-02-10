# Domain Model – Airline Fuel Optimization Agent

## Purpose
The domain layer defines the authoritative business entities used throughout
the system. These models are immutable and contain no business logic.

## Design Principles
- Immutability
- Explicit typing
- No side effects
- No infrastructure dependencies

## Domain Entities

### Flight
Represents a dispatched flight plan provided by airline systems.

Attributes:
- flight_id
- origin
- destination
- cruise_altitude_ft
- aircraft_type
- departure_time_utc

### AircraftPerformance
Represents static aircraft performance characteristics.

Attributes:
- aircraft_type
- fuel_burn_kg_per_hr (by altitude)

### Weather
Represents weather conditions relevant to fuel optimization.

Attributes:
- location
- wind_component_kt

## Non-Goals
- No optimization logic
- No validation logic
- No persistence logic
