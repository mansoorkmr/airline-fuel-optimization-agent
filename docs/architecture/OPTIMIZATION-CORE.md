# Optimization Core – Architecture

## Purpose
The optimization core determines fuel-efficient operational parameters
based on deterministic models and controlled inputs.

## Design Principles
- Pure computation
- Deterministic behavior
- No I/O or side effects
- Explainable outputs

## Components

### FuelConsumptionModel
Calculates hourly fuel burn using aircraft performance and weather data.

### FuelOptimizer
Evaluates candidate cruise altitudes and selects the optimal plan.

## Inputs
- AircraftService
- WeatherService
- AppSettings

## Outputs
- OptimizationResult (explicit, auditable)

## Non-Responsibilities
- No workflow orchestration
- No data ingestion
- No MCP publishing
