from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.appointment_service import get_appointment
from core.schemas import AppointmentRead

router = APIRouter()

@router.get("/appointments", response_model=list[AppointmentRead])
def get_appointments(db: Session = Depends(get_db)):
    appointments= get_appointment(db)
    return appointments
