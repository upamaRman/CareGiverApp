from fastapi import APIRouter, FastAPI, Depends, HTTPException
import src.schemas.medication_schema
import src.services.patient_services, src.models.patient_model, src.schemas.patient_schema
from src.db.db import get_db, engine
from sqlalchemy.orm import Session

from src.db.db import Base, engine
from src.models.patient_model import Patient
from src.models.medication_model import Medication
from src.schemas.patient_response_schema import PatientResponse



app = FastAPI()

router = APIRouter(prefix="/Patients", tags=["Patients"])

"""@router.get("/", response_model=list[PatientResponse])"""
@app.get("/Patients/", response_model=list[PatientResponse])
def get_all_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients




@app.post("/Patients/")
def create_new_patient(patient: src.schemas.patient_schema.PatientCreate, db: Session = Depends(get_db)):
    return src.services.patient_services.create_patient(db, patient)

