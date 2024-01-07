from fastapi import FastAPI
from starlette.middleware.trustedhost import TrustedHostMiddleware
from routers import user_router

apiServer = FastAPI()

apiServer.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],  # Replace with your actual domain(s)
)

apiServer.include_router(user_router.router)