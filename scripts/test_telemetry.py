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


driver_laps = session.laps.pick_drivers("VER")

fastest_lap = driver_laps.pick_fastest()

telemetry = fastest_lap.get_car_data().add_distance()


print("\nDRIVER")
print("VER")


print("\nFASTEST LAP")
print(fastest_lap["LapTime"])


print("\nTELEMETRY COLUMNS")
print(telemetry.columns.tolist())


print("\nTELEMETRY SAMPLE")
print(
    telemetry[
        [
            "Time",
            "Distance",
            "Speed",
            "RPM",
            "nGear",
            "Throttle",
            "Brake",
            "DRS",
        ]
    ].head(20)
)
