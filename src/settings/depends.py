from typing import AsyncGenerator
from src.settings.database import async_session


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
