from fastapi import FastAPI
from src.authorization.router import authorization_router
from src.registration.router import registration_router

authorization = FastAPI()

authorization.include_router(registration_router)
authorization.include_router(authorization_router)
