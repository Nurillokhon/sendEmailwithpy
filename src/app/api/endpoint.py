from fastapi import APIRouter

from .views import app

router = APIRouter()

router.include_router(app, prefix="/api", tags=["email"])
