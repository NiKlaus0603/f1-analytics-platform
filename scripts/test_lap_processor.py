from backend.app.data_engine.lap_processor import LapProcessor
from backend.app.data_engine.session_loader import SessionLoader


def main() -> None:
    loader = SessionLoader(
        year=2026,
        grand_prix="Italian Grand Prix",
        session_type="R",
    )

    loader.load()

    raw_laps = loader.get_laps()

    processor = LapProcessor(raw_laps)

    clean_laps = processor.clean()

    print("\n=== RAW LAP COUNT ===")
    print(len(raw_laps))

    print("\n=== CLEAN LAP COUNT ===")
    print(len(clean_laps))

    print("\n=== CLEAN COLUMNS ===")
    print(clean_laps.columns.tolist())

    print("\n=== CLEAN LAP SAMPLE ===")

    display_columns = [
        "Driver",
        "LapNumber",
        "LapTimeSeconds",
        "Compound",
        "TyreLife",
        "Stint",
        "Position",
    ]

    print(clean_laps[display_columns].head(15))

    print("\n=== NOR LAPS ===")

    nor_laps = processor.get_driver_laps("NOR")

    print(
        nor_laps[
            display_columns
        ].head(10)
    )

    print("\nNOR lap count:", len(nor_laps))

    print("\n=== ACCURATE LAPS ===")

    accurate_laps = processor.get_accurate_laps()

    print("Accurate lap count:", len(accurate_laps))

    print("\n=== QUICK LAPS ===")

    quick_laps = processor.get_quick_laps()

    print("Quick lap count:", len(quick_laps))

    if not quick_laps.empty:
        print(
            quick_laps[
                [
                    "Driver",
                    "LapNumber",
                    "LapTimeSeconds",
                    "Compound",
                    "TyreLife",
                ]
            ]
            .sort_values("LapTimeSeconds")
            .head(10)
        )


if __name__ == "__main__":
    main()
