from src.db.db import Base
from sqlalchemy import Integer, Column, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from src.models.patient_model import Patient

class Medication(Base):
    __tablename__ = 'medication'

    id = Column(Integer, primary_key = True, index= True)
    patient_id = Column(Integer, ForeignKey("patient.id"))
    medicine_name = Column(String, index =True)
    dosage = Column(String, index=True)
    frequency_per_day = Column(Integer)
    prescribed_date = Column(DateTime)
    duration_days = Column(Integer)
    instruction =Column(String)
    created_at = Column(DateTime, server_default=func.now())
    status =Column(String)

    patient = relationship("Patient", back_populates="medications")