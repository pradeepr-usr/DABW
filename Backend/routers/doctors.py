from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.doctor_service import get_doctors
from core.schemas import DoctorRead

router = APIRouter()

@router.get("/")
def read_doctors_root():            
    return {"message": "Doctors router is working"}

@router.get("/doctors", response_model=list[DoctorRead])
def get_all_doctors(db: Session = Depends(get_db)):
    doctors = get_doctors(db)
    return doctors
