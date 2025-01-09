from typing import Generic, TypeVar, Type, Optional, List, cast
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.base import Base
from sqlalchemy.sql import ColumnElement


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_by_id(self, entry_id: int) -> Optional[ModelType]:
        query = select(self.model).where(cast(ColumnElement[bool], self.model.id == entry_id))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self) -> List[ModelType]:
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, obj_in) -> ModelType:
        db_obj = self.model(**obj_in.dict())
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def update(self, entry_id: int, obj_in) -> Optional[ModelType]:
        db_obj = await self.get_by_id(entry_id)
        if db_obj:
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            await self.session.commit()
            await self.session.refresh(db_obj)
        return db_obj

    async def delete(self, entry_id: int) -> bool:
        db_obj = await self.get_by_id(entry_id)
        if db_obj:
            await self.session.delete(db_obj)
            await self.session.commit()
            return True
        return False