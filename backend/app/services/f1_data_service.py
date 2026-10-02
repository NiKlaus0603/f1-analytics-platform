import logging

import fastf1

from backend.app.core.config import settings


logger = logging.getLogger(__name__)


def configure_fastf1() -> None:
    fastf1.Cache.enable_cache(settings.F1_CACHE_DIR)

    logger.info(
        "FastF1 cache enabled at %s",
        settings.F1_CACHE_DIR,
    )


def load_session(year: int, grand_prix: str, session_type: str):
    logger.info(
        "Loading F1 session: %s %s %s",
        year,
        grand_prix,
        session_type,
    )

    session = fastf1.get_session(
        year,
        grand_prix,
        session_type,
    )

    session.load()

    logger.info(
        "F1 session loaded successfully: %s %s %s",
        year,
        grand_prix,
        session_type,
    )

    return session
