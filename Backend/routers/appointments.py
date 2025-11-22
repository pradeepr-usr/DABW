from fastapi import APIRouter

router = APIRouter()

@router.get("/appointments")
def get_appointments():
    return {"message": "List of appointments"}
