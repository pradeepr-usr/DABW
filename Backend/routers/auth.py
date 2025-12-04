from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from core.database import get_db
from services.auth_service import (
    create_user, create_patient, authenticate_user,
    create_access_token, create_refresh_token, decode_token
)
from core.schemas import UserCreate,PatientCreate, UserRead, Token, TokenRefreshRequest



router = APIRouter()

@router.get("/")
def read_auth_root():
    return {"message": "Auth router is working"}

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, patient: PatientCreate, db: Session = Depends(get_db)):
    # Set role to patient by default
    db_user = create_user(db, user, role="patient")
    # Link patient to user
    patient.user_id = db_user.id
    create_patient(db, patient)
    return db_user


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.username, "role": user.role})
    refresh_token = create_refresh_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}


@router.post("/refresh", response_model=Token)
def refresh_token(refresh_request: TokenRefreshRequest):
    payload = decode_token(refresh_request.refresh_token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    # Normally, also check if user exists in DB here (if required)
    new_access_token = create_access_token({"sub": username, "role": payload.get("role", "patient")})
    new_refresh_token = create_refresh_token({"sub": username})
    return {"access_token": new_access_token, "token_type": "bearer", "refresh_token": new_refresh_token}

