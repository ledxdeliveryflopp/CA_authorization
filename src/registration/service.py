from dataclasses import dataclass
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.registration.models import UserModel
from src.registration.repository import RegistrationRepository
from src.registration.schemas import CreateUserSchemas
from src.registration.utils import hash_password
from src.settings.depends import get_session
from src.settings.exception import UserExist
from src.vault.service import VaultService, get_vault_service


@dataclass
class RegistrationService(RegistrationRepository):
    """Сервис регистрации"""
    vault: VaultService

    async def create_user(self, schemas: CreateUserSchemas) -> dict:
        """Создание пользователя"""
        user = await self.find_user_by_email_or_mobile(email=schemas.email,  mobile=schemas.mobile)
        if user:
            raise UserExist
        user = UserModel(**schemas.model_dump(exclude=schemas.password))
        await self.session_save_object(user)
        await self.vault.create_secret(user_id=user.id, password=hash_password(schemas.password))
        return {"detail": "success"}


async def init_registration_service(session: AsyncSession = Depends(get_session),
                                    vault: VaultService = Depends(get_vault_service)) -> object:
    """инициализация сервиса регистрации"""
    service = RegistrationService(session=session, vault=vault)
    return service
