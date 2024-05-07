from dataclasses import dataclass
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class BaseRepository:
    """Базовый репозиторий для работы с БД"""
    session: AsyncSession

    async def session_save_object(self, saved_object: object) -> dict:
        """Сохрание объекта в БД"""
        try:
            self.session.add(saved_object)
            await self.session.commit()
            await self.session.refresh(saved_object)
        except IntegrityError:
            await self.session.rollback()
            return {"detail": "database exception"}
        except ProgrammingError:
            return {"detail": "database exception"}

    async def session_delete_object(self, deleted_object: object) -> dict:
        """Удаление из БД"""
        try:
            await self.session.delete(deleted_object)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            return {"detail": "database exception"}
        except ProgrammingError:
            return {"detail": "database exception"}
