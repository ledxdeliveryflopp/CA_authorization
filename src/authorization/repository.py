from dataclasses import dataclass
from sqlalchemy import Select
from src.registration.models import UserModel
from src.settings.service import BaseService


@dataclass
class AuthorizationRepository(BaseService):
    """Репозиторий авторизации"""

    async def find_user_by_email_or_mobile(self, email: str) -> UserModel:
        """Поиск пользователя по электронной почте или номеру телефона"""
        user = await self.session.execute(Select(UserModel).where(UserModel.email == email))
        return user.scalar()
