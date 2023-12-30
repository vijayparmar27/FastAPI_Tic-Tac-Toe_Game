from fastapi import APIRouter, Request
from models.user_model import SignupRequest
from connection.mongodb import mongoConnection

router = APIRouter(
    tags=["User"]    
)

# def index(request: SignupRequest):
@router.post("/signup")
def index(request: SignupRequest):
    print("signup :: request :: ", dict(request))
    return "........!!!!???"