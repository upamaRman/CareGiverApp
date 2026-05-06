from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from src.schemas.medication_schema import Medication

class Patient(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    status: Optional[str] = None
    medications: List[Medication]