"""
Operational Constraint Service.

Evaluates whether optimized plans are legally executable.
"""

from typing import Dict, List

from app.domain.constraints import AltitudeConstraint


class ConstraintService:
    def __init__(self, constraint_data: Dict):
        self._constraints = self._load(constraint_data)

    def _load(self, data: Dict) -> List[AltitudeConstraint]:
        constraints = []
        for item in data.get("altitude_constraints", []):
            constraints.append(
                AltitudeConstraint(
                    constraint_id=item["constraint_id"],
                    sector=item["sector"],
                    min_altitude_ft=item.get("min_altitude_ft"),
                    max_altitude_ft=item.get("max_altitude_ft"),
                    reason_code=item["reason_code"],
                    description=item["description"]
                )
            )
        return constraints

    def validate_altitude(
        self,
        sector: str,
        proposed_altitude_ft: int
    ) -> Dict:
        for constraint in self._constraints:
            if constraint.sector != sector:
                continue

            if constraint.min_altitude_ft is not None:
                if proposed_altitude_ft < constraint.min_altitude_ft:
                    return self._reject(constraint)

            if constraint.max_altitude_ft is not None:
                if proposed_altitude_ft > constraint.max_altitude_ft:
                    return self._reject(constraint)

        return {
            "allowed": True,
            "decision": "ALLOW",
            "reason": None,
            "message": "No operational constraints violated"
        }

    @staticmethod
    def _reject(constraint: AltitudeConstraint) -> Dict:
        return {
            "allowed": False,
            "decision": "REJECT",
            "reason": constraint.reason_code,
            "message": constraint.description
        }
