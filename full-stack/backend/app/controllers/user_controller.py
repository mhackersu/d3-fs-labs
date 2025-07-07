from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/")
def get_users():
    return [{"id": 1, "name": "Alice"}]
