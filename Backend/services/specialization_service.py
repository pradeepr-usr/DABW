# services/specialization_service.py

from sqlalchemy.orm import Session
from core import models, schemas

def create_specialization(db: Session, specialization_in: schemas.SpecializationCreate) -> models.Specialization:
    specialization = models.Specialization(name=specialization_in.name)
    db.add(specialization)
    db.commit()
    db.refresh(specialization)
    return specialization

def get_specializations(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Specialization)
        .offset(skip)
        .limit(limit)
        .all()
    )
