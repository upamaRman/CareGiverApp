from datetime import date
from typing import List, Optional
from app.models.medication import Medication
from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    status: Optional[str] = None
    medications: List[Medication] = []

    class Config:
        from_attributes = True