from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.config import settings
from src.db.deps import get_db
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/api/v1/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

@app.get("/api/v1/health")
async def health_check(db: AsyncSession = Depends(get_db())):
    try:
        await db.execute("SELECT 1")
        return {"status": "ok", "database": "connected"}
    except Exception:
        return {"status": "error", "database": "disconnected"}

if __name__ == "main":
    uvicorn.run(app, host="0.0.0.0", port=8000)