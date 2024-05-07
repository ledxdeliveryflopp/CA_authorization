from pydantic import BaseModel, EmailStr


class LoginSchemas(BaseModel):
    """Схема логина"""
    email: EmailStr
    password: str


class TokenSchemas(BaseModel):
    """Схема токена"""
    access_token: str
