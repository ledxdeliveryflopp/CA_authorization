from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class BaseSchemas(BaseModel):
    """Абстрактная схема пользователя"""

    name: str
    surname: str
    email: EmailStr
    mobile: str = Field(max_length=15)
    description: Optional[str]
    city: str
    birthday: date


class CreateUserSchemas(BaseSchemas):
    """Схема регистрации пользователя"""
    password: str = Field(min_length=6)
