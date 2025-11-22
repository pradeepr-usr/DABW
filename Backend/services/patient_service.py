from sqlalchemy.orm import Session
from core.models import Patient
from core.schemas import PatientCreate

# --- Patient CRUD ---
def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_patient_by_user_id(db: Session, user_id: int):
    return db.query(Patient).filter(Patient.user_id == user_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

