from fastapi import APIRouter, Request, Header, Depends
from models.user_model import SignupRequest, LoginRequest
from controllers.user_controller import signupController, loginController
from utils.token import Token

router = APIRouter(
    tags=["User"]
)


@router.post("/signup")
async def signupReq(request: SignupRequest):
    data = await signupController(request)
    return data


@router.post("/login")
async def loginReq(request: LoginRequest):
    data = await loginController(request)
    return data


@router.get("/users", dependencies=[Depends(Token.verify_token)])
def users(request: Request):
    print("request :: ", request.state.payload)
    return "...."

