import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "F1 Analytics Platform")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    F1_CACHE_DIR = os.getenv("F1_CACHE_DIR", "data/cache")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./data/f1_analytics.db",
    )


settings = Settings()
