from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_users_root():
    return {"message": "Users router is working"}   