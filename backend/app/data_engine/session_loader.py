import logging
from typing import Any

from backend.app.services.f1_data_service import load_session


logger = logging.getLogger(__name__)


class SessionLoader:
    """Load and expose Formula 1 session data."""

    def __init__(
        self,
        year: int,
        grand_prix: str,
        session_type: str,
    ) -> None:
        self.year = year
        self.grand_prix = grand_prix
        self.session_type = session_type
        self.session = None

    def load(self) -> Any:
        """Load the requested FastF1 session."""

        logger.info(
            "Data Engine loading session: %s %s %s",
            self.year,
            self.grand_prix,
            self.session_type,
        )

        self.session = load_session(
            self.year,
            self.grand_prix,
            self.session_type,
        )

        return self.session

    def _require_session(self) -> Any:
        if self.session is None:
            raise RuntimeError(
                "Session has not been loaded. Call load() first."
            )

        return self.session

    def get_laps(self):
        """Return all available lap data."""

        session = self._require_session()
        return session.laps

    def get_weather(self):
        """Return session weather data."""

        session = self._require_session()
        return session.weather_data

    def get_results(self):
        """Return session classification/results."""

        session = self._require_session()
        return session.results

    def get_drivers(self) -> list[str]:
        """Return driver identifiers for the session."""

        session = self._require_session()
        return list(session.drivers)

    def get_session_info(self) -> dict[str, Any]:
        """Return basic metadata describing the loaded session."""

        session = self._require_session()

        event = session.event

        return {
            "year": self.year,
            "grand_prix": self.grand_prix,
            "session_type": self.session_type,
            "event_name": event.get("EventName"),
            "official_event_name": event.get("OfficialEventName"),
            "country": event.get("Country"),
            "location": event.get("Location"),
            "round_number": event.get("RoundNumber"),
        }
