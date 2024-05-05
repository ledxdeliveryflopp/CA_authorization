from dataclasses import dataclass
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class BaseRepository:
    """Базовый репозиторий для работы с БД"""
    session: AsyncSession

    async def session_save_object(self, saved_object: object) -> None:
        """Сохрание объекта в БД"""
        try:
            self.session.add(saved_object)
            await self.session.commit()
            await self.session.refresh(saved_object)
        except IntegrityError:
            await self.session.rollback()

    async def session_delete_object(self, deleted_object: object) -> None:
        """Удаление из БД"""
        try:
            await self.session.delete(deleted_object)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
