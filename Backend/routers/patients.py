from fastapi import APIRouter
from services.patient_service import get_patients  # Import the function
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from core.schemas import PatientRead 
from routers.dependencies import require_roles


router = APIRouter()

@router.get("/")
def read_patients_root():
    return {"message": "Patients router is working"}


@router.get("/patients", response_model=list[PatientRead])
def get_all_patients(
    db: Session = Depends(get_db),
    _: None = Depends(require_roles("admin")),   # only admin can see all patients
):
    patients = get_patients(db)
    return patients
