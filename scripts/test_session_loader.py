from backend.app.data_engine.session_loader import SessionLoader


def main() -> None:
    loader = SessionLoader(
        year=2026,
        grand_prix="Italian Grand Prix",
        session_type="R",
    )

    session = loader.load()

    print("\n=== SESSION INFO ===")
    print(loader.get_session_info())

    print("\n=== DRIVERS ===")
    print(loader.get_drivers())

    print("\n=== LAPS ===")
    laps = loader.get_laps()
    print(laps.head())

    print("\n=== WEATHER ===")
    weather = loader.get_weather()
    print(weather.head())

    print("\n=== RESULTS ===")
    results = loader.get_results()

    columns = [
        column
        for column in ["Position", "Abbreviation", "TeamName", "Status"]
        if column in results.columns
    ]

    print(results[columns].head(10))

    print("\n=== SESSION OBJECT ===")
    print(type(session))


if __name__ == "__main__":
    main()
