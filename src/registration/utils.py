from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Хэширование пароля"""
    return context.hash(password)