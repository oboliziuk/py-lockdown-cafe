import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
