from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicationCreate(BaseModel):
    medicine_name : str
    dosage : Optional[str]
    frequency_per_day : Optional[int]
    prescribed_date : Optional[date]
    duration_days : Optional[int]
    instruction : Optional[str]
    status : Optional[str] 
