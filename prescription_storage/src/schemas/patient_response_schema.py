from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class MedicationResponse(BaseModel):
    id: int
    medicine_name: Optional[str]
    dosage: Optional[str]
    frequency_per_day: Optional[int]
    prescribed_date: Optional[date]
    duration_days: Optional[int]
    instruction: Optional[str]
    status: Optional[str]

    class Config:
        from_attributes = True


class PatientResponse(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    status: Optional[str]
    medications: List[MedicationResponse] = []

    class Config:
        from_attributes = True