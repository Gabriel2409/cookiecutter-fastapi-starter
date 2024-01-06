from app.routers import healthcheck
from fastapi import FastAPI


def create_app():
    """Creates the FastAPI app"""
    app = FastAPI()
    app.include_router(healthcheck.router)
    return app
