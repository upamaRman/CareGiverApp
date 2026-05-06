from datetime import datetime
from app.models.patient import Patient
from app.models.patient_message import PatientMessage
from app.service import patient_service 
from typing import List


def get_message():
    
    patients : List[Patient] = patient_service.get_all_patients()
    return format_messages(patients)




def format_messages(patients: List[Patient]):
    patient_message_dict = []

    for patient in patients:
        patient_id : int = patient.id  # int variable from patient object

        message_lines = [f"Patient: {patient.first_name} {patient.last_name}"]

        for med in patient.medications:
            med_line = (
                f"- Medication: {med.medicine_name}, "
                f"Dosage: {med.dosage}, "
                f"Frequency: {med.frequency_per_day}, "
                f"Instructions: {med.instruction}"
            )
            message_lines.append(med_line)

        full_message = "\n".join(message_lines)

        patient_message_dict.append({
            "patient_id": patient_id,
            "patient_message": full_message
        })

    return patient_message_dict


