from dataclasses import dataclass
from typing import Coroutine
from src.settings.repository import BaseRepository


@dataclass
class BaseService(BaseRepository):
    """Базовый сервис для работы с БД"""

    async def save_object(self, saved_object: object) -> Coroutine:
        """Сохранение объекта"""
        return await self.session_save_object(saved_object)

    async def delete_object(self, deleted_object: object) -> Coroutine:
        """Удаление объекта"""
        return await self.session_delete_object(deleted_object)

