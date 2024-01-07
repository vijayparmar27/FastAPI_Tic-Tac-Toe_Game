from pydantic import BaseModel


class SignupRequest(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    userName: str | None = None
    phoneNo: str | None = None
    password: str | None = None
    confPassword: str | None = None


class LoginRequest(BaseModel):
    uniqueId: str | None = None
    password: str | None = None



