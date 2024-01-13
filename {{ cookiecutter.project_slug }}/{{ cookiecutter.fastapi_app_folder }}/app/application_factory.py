import logging.config

from app.routers import healthcheck
from fastapi import FastAPI

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


def create_app():
    """Creates the FastAPI app"""
    app = FastAPI()
    app.include_router(healthcheck.router)
    return app
