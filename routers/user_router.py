from fastapi import APIRouter, Request, Header, Depends
from models.user_model import SignupRequest, LoginRequest
from controllers.user_controller import signupController, loginController
from utils.token import Token
from config.config import port_value
from constant.massages.index import MESSAGES

router = APIRouter(
    tags=["Users"]
)

@router.get("/test")
def test():
    # print("PORT ::: ",port_value , type(port_value))
    # print("PORT ::: ",port_value.key)
    # print("CONSTANT ::: ",MESSAGES.POPUP)
    # print("CONSTANT ::: ",MESSAGES.POPUP.POPUP_TYPE)
    # print("CONSTANT ::: ",MESSAGES.POPUP.POPUP_TYPE.COMMON_POPUP)
    # print("CONSTANT ::: ",CONSTANT.EVENT.SIGN_UP)
    return "ok....."


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

