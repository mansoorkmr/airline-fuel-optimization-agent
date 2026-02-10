# Ingestion Layer – Architecture

## Purpose
The ingestion layer is responsible for loading external data sources
and converting them into immutable domain entities.

## Responsibilities
- Read external inputs (CSV, API, DB)
- Map raw data to domain models
- Perform basic structural validation

## Non-Responsibilities
- No optimization logic
- No enrichment
- No business rules
- No persistence

## Current Implementation
- CSV-based flight ingestion

## Future Extensions
- Airline API integration
- Streaming ingestion
- Database-backed repositories
