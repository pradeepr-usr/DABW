# routers/specializations.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers.dependencies import require_roles

from core import schemas
from core.database import get_db
from services import specialization_service

router = APIRouter(prefix="/specializations", tags=["Specializations"])

@router.post("/", response_model=schemas.SpecializationRead)
def create_specialization(
    specialization_in: schemas.SpecializationCreate,
    db: Session = Depends(get_db),
    _: None = Depends(require_roles("admin"))
):
    return specialization_service.create_specialization(db, specialization_in)

@router.get("/", response_model=list[schemas.SpecializationRead])
def list_specializations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _: None = Depends(require_roles("admin"))
):
    return specialization_service.get_specializations(db, skip=skip, limit=limit)
