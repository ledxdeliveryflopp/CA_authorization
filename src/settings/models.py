from sqlalchemy import Column, Integer, DateTime, func
from src.settings.database import Base


class AbstractModel(Base):
    """Абстрактная модель"""
    __abstract__ = True

    id = Column(Integer,  primary_key=True, nullable=False, autoincrement=True, unique=True,
                index=True, comment="ID")
    created_at = Column(DateTime, server_default=func.now())
