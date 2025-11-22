from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Patient Schemas
class PatientBase(BaseModel):
    first_name: str
    last_name: str
    dob: Optional[datetime]
    gender: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class PatientCreate(PatientBase):
    user_id: int

class PatientRead(PatientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Repeat similar structure for Doctor, Appointment, Review, etc.

