from dataclasses import dataclass
from sqlalchemy import Select, or_
from src.registration.models import UserModel
from src.settings.service import BaseService


@dataclass
class RegistrationRepository(BaseService):
    """Репозиторий регистрации"""

    async def find_user_by_email_or_mobile(self, email: str, mobile: str) -> UserModel:
        """Поиск пользователя по электронной почте или номеру телефона"""
        user = await self.session.execute(Select(UserModel).where(or_(UserModel.email == email,
                                                                      UserModel.mobile == mobile)))
        return user.scalar()

