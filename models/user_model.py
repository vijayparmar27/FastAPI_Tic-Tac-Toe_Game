from pydantic import BaseModel


class SignupRequest(BaseModel):
    firstName: str
    lastName: str
    userName: str
    phoneNo: str
    password: str
    confPassword: str
