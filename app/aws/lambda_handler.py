"""
AWS Lambda handler for airline fuel optimization.
"""

import json
from app.hpc.flight_task import main as run_flight_task


def handler(event, context):
    """
    Lambda entry point.

    Expects:
    {
      "flight_index": int
    }
    """
    flight_index = int(event["flight_index"])
    run_flight_task(flight_index)

    return {
        "status": "SUCCESS",
        "flight_index": flight_index
    }
