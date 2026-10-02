from backend.app.services.f1_data_service import (
    configure_fastf1,
    load_session,
)


configure_fastf1()

session = load_session(
    year=2025,
    grand_prix="Monza",
    session_type="R",
)


print("\nSESSION")
print(session.event["EventName"])


print("\nDRIVERS")
print(session.drivers)


print("\nRESULTS")
print(
    session.results[
        [
            "Abbreviation",
            "TeamName",
            "GridPosition",
            "Position",
            "Points",
        ]
    ].head(10)
)


print("\nLAPS")
print(
    session.laps[
        [
            "Driver",
            "LapNumber",
            "LapTime",
            "Compound",
            "TyreLife",
        ]
    ].head(10)
)


print("\nWEATHER")
print(session.weather_data.head())
