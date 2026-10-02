import logging

from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.core.logging import setup_logging


setup_logging()

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered Formula 1 analytics and prediction platform",
    version=settings.APP_VERSION,
)


@app.on_event("startup")
def startup_event():
    logger.info(
        "%s starting in %s environment",
        settings.APP_NAME,
        settings.APP_ENV,
    )


@app.get("/")
def root():
    logger.info("Root endpoint requested")

    return {
        "project": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "status": "running",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
