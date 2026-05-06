from pydantic import BaseModel
from src.schemas.medication_schema import MedicationCreate
from typing import List, Optional
from datetime import date

class PatientCreate(BaseModel) :
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    status: Optional[str] = None
    medications: List[MedicationCreate]



