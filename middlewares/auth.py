from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Request, Depends, FastAPI, HTTPException, status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30000


class Token:

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def verify_token(request: Request):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials")
        
        token = request.headers.get("token")
        payload = await jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("_id")
        if id is None:
            raise credentials_exception
        request.state.payload = payload
        return request
    
    @staticmethod
    async def verify_token_for_event(token:str):
        try:
            # Decode the JWT with the appropriate secret key and algorithms
            payload =  jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            print("----- verify_token_for_event :: payload :: ",payload)
            id: str = payload.get("id")
            if id is None:
                return False
            return id
        except JWTError as ex:
            return False
