# Ingestion Scope & Boundaries

## Purpose
This document defines the authoritative scope of data ingestion
for the Airline Fuel Optimization Agent POC.

## Authoritative Inputs
- Flight plans: CSV-based input (`data/flights.csv`)
- Weather data: Mocked JSON payload
- Aircraft performance: Mocked JSON payload

## Design Rationale
CSV ingestion was selected to ensure:
- Deterministic inputs
- Easy reproducibility
- Minimal external dependencies

This choice is intentional and aligned with POC best practices.

## Weather Data Scope
Weather data represents an abstracted METAR/TAF signal in the form
of wind components relevant to fuel optimization.

- No raw METAR/TAF strings are parsed
- WeatherService API is stable and replaceable
- Real METAR/TAF ingestion requires no refactor

## Aircraft Performance Scope
Aircraft performance data is simulated using static lookup tables.
This reflects typical manufacturer-provided performance envelopes.

## Explicit Non-Scope
- Live API ingestion
- Real-time weather streaming
- Vendor-specific airline feeds

These are deferred by design and documented as extensions.
