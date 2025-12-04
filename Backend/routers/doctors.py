from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.doctor_service import get_doctors, create_doctor
from services.auth_service import create_user
from core.schemas import DoctorRead, DoctorCreate, UserCreate
from routers.dependencies import require_roles

router = APIRouter()

@router.get("/")
def read_doctors_root():            
    return {"message": "Doctors router is working"}

@router.get("/doctors", response_model=list[DoctorRead])
def get_all_doctors(
    db: Session = Depends(get_db), 
    _: None = Depends(require_roles("admin"))):
    doctors = get_doctors(db)
    return doctors

@router.post("/doctors", response_model=DoctorRead)
def add_doctor(
    user: UserCreate,
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
    _: None = Depends(require_roles("admin")),   # admin-only
):
    db_user = create_user(db, user, role="doctor")
    doctor.user_id = db_user.id
    db_doctor = create_doctor(db, doctor)
    return db_doctor


