from sqlalchemy import Column, String, DateTime
from src.settings.models import AbstractModel


class TokenModel(AbstractModel):
    """Модель токена"""
    __tablename__ = "token"

    token = Column(String, nullable=False, index=True, comment="Токен")
    expire = Column(DateTime, nullable=False, comment="Срок действия")
