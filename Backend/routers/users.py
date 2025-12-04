# routers/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from services.auth_service import create_user
from services.user_services import get_users 
from core.schemas import UserCreate, UserRead
from routers.dependencies import require_roles

router = APIRouter()

@router.get("/")
def read_users_root():
    return {"message": "Users router is working"}

@router.get("/users", response_model=list[UserRead])
def get_all_users(
    db: Session = Depends(get_db),
    _: None = Depends(require_roles("admin")),
):
    users = get_users(db)
    return users

@router.post("/add_admin", response_model=UserRead)
def add_admin(
    user: UserCreate, 
    db: Session = Depends(get_db),
    _: None = Depends(require_roles("admin")),
    ):
    # Create user with role=admin
    db_user = create_user(db, user, role="admin")
    return db_user

  