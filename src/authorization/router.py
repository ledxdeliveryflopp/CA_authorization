from fastapi import APIRouter, Depends
from src.authorization.schemas import TokenSchemas, LoginSchemas
from src.authorization.service import AuthorizationService, init_authorization_service

authorization_router = APIRouter(prefix='/authorization', tags=['authorization'])


@authorization_router.post("/login/", response_model=TokenSchemas)
async def login_router(schemas: LoginSchemas, service: AuthorizationService = Depends(
                       init_authorization_service)):
    """Роутер авторизации"""
    return await service.login(schemas)