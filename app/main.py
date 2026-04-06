from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.auctions import router as auctions_router
from app.api.routes.characters import router as characters_router
from app.api.routes.health import router as health_router
from app.db.init_db import init_db

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health_router)
app.include_router(auctions_router)
app.include_router(characters_router)


@app.get("/")
def read_root():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV
    }
