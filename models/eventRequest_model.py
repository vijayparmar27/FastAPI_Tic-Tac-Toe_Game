from pydantic import BaseModel
from typing import Optional


class signupEventReq(BaseModel):
    token: Optional[str] = None
    name: str | None = None