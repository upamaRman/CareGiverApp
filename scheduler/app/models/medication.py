from datetime import date
from pydantic import BaseModel
from typing import Optional

class Medication(BaseModel):
    id: int
    medicine_name: Optional[str]
    dosage : Optional[str]
    frequency_per_day : Optional[int]  = None
    prescribed_date : Optional[date] = None
    duration_days : Optional[int] = None
    instruction : Optional[str] = None
    status : Optional[str] = None


    class Config:
        from_attributes = True    