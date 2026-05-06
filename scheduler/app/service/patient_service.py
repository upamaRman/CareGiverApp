import httpx
from typing import List, Dict
from app.models.patient import Patient

BASE_URL = "http://localhost:8001"  # adjust if needed

def get_all_patients() -> List[Patient]:
    with httpx.Client(timeout=10.0) as client:
        response = client.get(f"{BASE_URL}/Patients/")
        response.raise_for_status()
        data = response.json()  # this is a list of dicts

        return [Patient(**patient) for patient in data]
