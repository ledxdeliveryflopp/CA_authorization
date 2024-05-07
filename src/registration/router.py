from fastapi import APIRouter, Depends
from src.registration.schemas import CreateUserSchemas
from src.registration.service import RegistrationService, init_registration_service

registration_router = APIRouter(prefix="/registration", tags=["registration"])


@registration_router.post("/register/")
async def create_user_router(schemas: CreateUserSchemas, service: RegistrationService = Depends(
                              init_registration_service)):
    """Роутер регистрации"""
    return await service.create_user(schemas)

