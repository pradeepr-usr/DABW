from fastapi import APIRouter
from services.patient_service import get_patient  # Import the function
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from core.schemas import PatientRead 


router = APIRouter()

@router.get("/")
def read_patients_root():
    return {"message": "Patients router is working"}


@router.get("/patients", response_model=list[PatientRead])  # Use your schema for proper docs/validation
def get_all_patients(db: Session = Depends(get_db)):
    patients = get_patient(db)
    return patients
