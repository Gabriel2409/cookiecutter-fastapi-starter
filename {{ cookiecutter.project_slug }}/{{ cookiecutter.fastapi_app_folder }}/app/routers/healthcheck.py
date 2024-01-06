from typing import Annotated

from app.config import Settings, get_settings
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/")
def hello(settings: Annotated[Settings, Depends(get_settings)]):
    """Hello world route"""
    return {
        "msg": "Hello World!",
        "app_name": settings.app_name,
        "env": settings.env,
    }


@router.get("/healthcheck")
def healthcheck():
    """Health check route"""
    return {"msg": "ok"}
