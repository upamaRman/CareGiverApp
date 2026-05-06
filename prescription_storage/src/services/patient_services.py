from src.models.patient_model import Patient
from src.models.medication_model import Medication
from sqlalchemy.orm import Session
from src.schemas.patient_schema import PatientCreate 

def create_patient(db: Session, patient: PatientCreate) : 
    patient_instance = Patient(
        first_name=patient.first_name,
        last_name=patient.last_name,
        gender=patient.gender,
        dob=patient.dob,
        status = 'Active'
        )
    db.add(patient_instance)
    db.commit()
    db.refresh(patient_instance)

    for med in patient.medications:
        db_med = Medication(
            medicine_name=med.medicine_name,
            dosage=med.dosage,
            frequency_per_day=med.frequency_per_day,
            prescribed_date=med.prescribed_date,
            instruction=med.instruction,
            patient_id=patient_instance.id,
            duration_days = med.duration_days,
            status = 'Active'
        )
        db.add(db_med)
    db.commit()

    db.refresh(patient_instance)
    return {"patient_id": patient_instance.id, "message": "Patient and medications created successfully"}


