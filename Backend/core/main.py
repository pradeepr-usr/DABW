from fastapi import FastAPI
from routers import auth, users, doctors, patients, appointments  # Import your route modules here
from core.database import engine, Base
from core.create_db_and_user import create_database_and_user

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Doctor Appointment Booking System")

@app.on_event("startup")
def on_startup():
    create_database_and_user()  # Run create DB/user logic on startup
    Base.metadata.create_all(bind=engine)  # Create tables

# Include your routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Doctor Appointment Booking API"}

