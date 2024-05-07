import random
import string
from dataclasses import dataclass
from datetime import datetime, timedelta
from fastapi import Depends
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from src.authorization.models import TokenModel
from src.authorization.repository import AuthorizationRepository
from src.authorization.schemas import LoginSchemas
from src.authorization.utils import verify_password
from src.settings.depends import get_session
from src.settings.exception import UserDontExist
from src.settings.settings import settings
from src.vault.service import VaultService, get_vault_service


@dataclass
class AuthorizationService(AuthorizationRepository):
    """Сервис авторизации"""
    vault: VaultService

    async def create_token(self, email: str) -> TokenModel:
        """Создание токена"""
        expire = datetime.utcnow() + timedelta(minutes=30)
        random_string = random.choices(string.printable, k=10)
        data = {"user_email": email, "randon": random_string}
        token = jwt.encode(data, settings.token_settings.secret,
                           algorithm=settings.token_settings.algorithm)
        new_token = TokenModel(token=token, expire=expire)
        await self.session_save_object(new_token)
        return new_token

    async def login(self, schemas: LoginSchemas) -> dict:
        """Авторизация"""
        user = await self.find_user_by_email_or_mobile(schemas.email)
        if not user:
            raise UserDontExist
        password_from_vault = await self.vault.read_secret(user.id)
        password = await verify_password(schemas.password, password_from_vault)
        if not password:
            raise UserDontExist
        token = await self.create_token(schemas.email)
        return {"access_token": token.token}


async def init_authorization_service(session: AsyncSession = Depends(get_session),
                                     vault: VaultService = Depends(get_vault_service)) -> object:
    """Инициализация сервиса токенов"""
    service = AuthorizationService(session, vault)
    return service
