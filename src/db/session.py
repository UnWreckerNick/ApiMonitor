from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.core.config import settings

DATABASE_URL = settings.DATABASE_URL.replace('sqlite:///', 'sqlite+aiosqlite:///', 1)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)