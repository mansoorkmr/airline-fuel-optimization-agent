# METAR/TAF Integration Extension Blueprint

## Purpose
Define how real METAR/TAF data would be integrated without
changing core optimization logic.

## Integration Point
- Module: `app/services/weather_service.py`
- Replace mock payload with parsed METAR/TAF feed

## Parsing Strategy
- Use NOAA / ICAO compliant METAR libraries
- Convert raw METAR/TAF to structured wind components

## Architectural Guarantee
- No changes to FuelConsumptionModel
- No changes to optimization core
- WeatherService remains the sole boundary

## Rationale
This preserves determinism while enabling future realism.
