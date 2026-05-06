
from dataclasses import dataclass
from typing import Optional

@dataclass
class PatientMessage():
    patient_id : int
    patient_message : Optional[str]