from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Medication(BaseModel):
    medicine_name : str
    dosage : Optional[str]
    frequency_per_day : Optional[int]  = None
    prescribed_date : Optional[date] = None
    duration_days : Optional[int] = None
    instruction : Optional[str] = None
    status : Optional[str] = None


