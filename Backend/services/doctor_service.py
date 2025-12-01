from sqlalchemy.orm import Session
from core.models import Doctor
from core.schemas import DoctorCreate

# --- Doctor CRUD ---
def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_doctor_by_user_id(db: Session, user_id: int):
    return db.query(Doctor).filter(Doctor.user_id == user_id).first()

def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Doctor).offset(skip).limit(limit).all()

def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = Doctor(
        user_id=doctor.user_id,
        specialization_id=doctor.specialization_id,
        first_name=doctor.first_name,
        last_name=doctor.last_name,
        qualification=doctor.qualification,
        hospital_affiliation=doctor.hospital_affiliation,
        phone=doctor.phone,
        address=doctor.address
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor
