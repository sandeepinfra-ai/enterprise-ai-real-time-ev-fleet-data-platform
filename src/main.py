from fastapi import FastAPI

from src.api.v1.health import router as health_router
from src.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "environment": settings.app_env,
        "version": settings.app_version,
    }