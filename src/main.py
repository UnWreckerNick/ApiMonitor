from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings, get_settings
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
async def health_check():
    return {"status": "ok"}

if __name__ == "main":
    uvicorn.run(app, host="0.0.0.0", port=8000)