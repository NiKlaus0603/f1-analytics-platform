import logging

import pandas as pd


logger = logging.getLogger(__name__)


class LapProcessor:
    """Clean and transform raw FastF1 lap data."""

    LAP_COLUMNS = [
        "Driver",
        "DriverNumber",
        "LapNumber",
        "LapTime",
        "Sector1Time",
        "Sector2Time",
        "Sector3Time",
        "Stint",
        "Compound",
        "TyreLife",
        "FreshTyre",
        "Position",
        "PitInTime",
        "PitOutTime",
        "SpeedI1",
        "SpeedI2",
        "SpeedFL",
        "SpeedST",
        "IsPersonalBest",
        "IsAccurate",
    ]

    def __init__(self, laps: pd.DataFrame) -> None:
        self.raw_laps = laps.copy()
        self.laps: pd.DataFrame | None = None

    @staticmethod
    def _timedelta_to_seconds(series: pd.Series) -> pd.Series:
        """Convert timedelta values to floating-point seconds."""

        return series.dt.total_seconds()

    def clean(self) -> pd.DataFrame:
        """Select useful columns and create numeric timing features."""

        logger.info(
            "Cleaning lap data: %s raw laps",
            len(self.raw_laps),
        )

        available_columns = [
            column
            for column in self.LAP_COLUMNS
            if column in self.raw_laps.columns
        ]

        laps = self.raw_laps[available_columns].copy()

        timing_columns = {
            "LapTime": "LapTimeSeconds",
            "Sector1Time": "Sector1Seconds",
            "Sector2Time": "Sector2Seconds",
            "Sector3Time": "Sector3Seconds",
        }

        for source_column, target_column in timing_columns.items():
            if source_column in laps.columns:
                laps[target_column] = self._timedelta_to_seconds(
                    laps[source_column]
                )

        numeric_columns = [
            "LapNumber",
            "Stint",
            "TyreLife",
            "Position",
            "SpeedI1",
            "SpeedI2",
            "SpeedFL",
            "SpeedST",
        ]

        for column in numeric_columns:
            if column in laps.columns:
                laps[column] = pd.to_numeric(
                    laps[column],
                    errors="coerce",
                )

        self.laps = laps.reset_index(drop=True)

        logger.info(
            "Lap data cleaned successfully: %s laps",
            len(self.laps),
        )

        return self.laps

    def _require_clean_laps(self) -> pd.DataFrame:
        if self.laps is None:
            return self.clean()

        return self.laps

    def get_driver_laps(self, driver: str) -> pd.DataFrame:
        """Return cleaned laps for one driver."""

        laps = self._require_clean_laps()

        driver = driver.upper()

        return laps[
            laps["Driver"].astype(str).str.upper() == driver
        ].copy()

    def get_accurate_laps(self) -> pd.DataFrame:
        """Return laps FastF1 marks as accurate."""

        laps = self._require_clean_laps()

        if "IsAccurate" not in laps.columns:
            return laps.copy()

        return laps[laps["IsAccurate"] == True].copy()  # noqa: E712

    def get_quick_laps(
        self,
        threshold: float = 1.07,
    ) -> pd.DataFrame:
        """
        Return laps within a percentage of the fastest lap.

        A threshold of 1.07 keeps laps no slower than 107%
        of the fastest valid lap.
        """

        laps = self.get_accurate_laps()

        laps = laps.dropna(
            subset=["LapTimeSeconds"]
        ).copy()

        if laps.empty:
            return laps

        fastest_lap = laps["LapTimeSeconds"].min()

        return laps[
            laps["LapTimeSeconds"]
            <= fastest_lap * threshold
        ].copy()
