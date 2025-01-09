from typing import List, cast
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.endpoint import Endpoint
from src.db.repositories.base import BaseRepository
from sqlalchemy.sql import ColumnElement

class EndpointRepository(BaseRepository[Endpoint]):
    def __init__(self, db: AsyncSession):
        super().__init__(Endpoint, db)

    async def get_by_user(self, user_id: int) -> List[Endpoint]:
        query = select(self.model).where(cast(ColumnElement[bool], self.model.user_id == user_id))
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_active_endpoints(self) -> List[Endpoint]:
        query = select(self.model).join(cast(ColumnElement[bool], self.model.user).where(
            self.model.user.is_active == True
        ))
        result = await self.db.execute(query)
        return result.scalars().all()