from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Authentication Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class TokenRefreshRequest(BaseModel):
    refresh_token: str

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

    model_config = {
        "from_attributes": True
    }

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

    model_config = {
        "from_attributes": True
    }

#doctor Schemas
class DoctorBase(BaseModel):
    user_id: int
    specialization_id: int
    first_name: str
    last_name: str
    qualification: Optional[str]
    hospital_affiliation: Optional[str]
    phone: Optional[str]
    address: Optional[str]


class DoctorCreate(DoctorBase):
    pass

class DoctorRead(DoctorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

# Appointment Schemas
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    status: Optional[str]
    reason: Optional[str]


class AppointmentCreate(AppointmentBase):
    pass

class AppointmentRead(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

# Specialization Schemas

class SpecializationBase(BaseModel):
    name: str                   
class SpecializationCreate(SpecializationBase):
    pass                
class SpecializationRead(SpecializationBase):
    id: int

    model_config = {
        "from_attributes": True
    }
    
# Review Schemas
class ReviewBase(BaseModel):
    patient_id: int
    doctor_id: int
    rating: int
    comment: Optional[str]
class ReviewCreate(ReviewBase):
    pass
class ReviewRead(ReviewBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

        
# Availability Schemas
class AvailabilityBase(BaseModel):
    doctor_id: int
    day_of_week: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]
    is_available: Optional[bool] = True
class AvailabilityCreate(AvailabilityBase):
    pass
class AvailabilityRead(AvailabilityBase):
    id: int

    model_config = {
        "from_attributes": True
    }

        
# Billing Schemas
class BillingBase(BaseModel):
    appointment_id: int
    amount: float
    payment_status: Optional[str]
    payment_method: Optional[str]
class BillingCreate(BillingBase):
    pass
class BillingRead(BillingBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


#notification Schemas
class NotificationBase(BaseModel):
    user_id: int
    message: str
    type: Optional[str]
    is_read: Optional[bool] = False
class NotificationCreate(NotificationBase):
    pass
class NotificationRead(NotificationBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

