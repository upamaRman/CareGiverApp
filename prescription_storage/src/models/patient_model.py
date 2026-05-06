from src.db.db import Base
from sqlalchemy import Integer, Column, String , DateTime, func
from sqlalchemy.orm import relationship, declarative_base

class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String, index=True)
    dob = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    status = Column(String)

    medications = relationship(
        "Medication",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

