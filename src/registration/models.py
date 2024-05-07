from sqlalchemy import Column, String, DateTime
from src.settings.models import AbstractModel


class UserModel(AbstractModel):
    """Модель пользователя"""
    __tablename__ = "user"

    name = Column(String, nullable=False, index=True, comment="Имя")
    surname = Column(String, nullable=False, index=True, comment="Фамилия")
    email = Column(String, nullable=False, index=True, comment="Электронная почта")
    mobile = Column(String(15), nullable=False, comment="Номер телефона")
    status = Column(String(length=50), nullable=True, comment="Короткий статус")
    description = Column(String, nullable=True, comment="Описание профиля")
    city = Column(String, nullable=True, index=True, comment="Родной город")
    birthday = Column(DateTime, nullable=False, comment="Дата рождения")
