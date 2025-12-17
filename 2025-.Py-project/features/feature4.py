# feature4.py — Top 5 Games by Region Leaderboards


# CLI version
def top_five_games_by_region(database):
    """
    Print top 5 games for each region.
    """
    regions = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Other_Sales": "Other Regions",
        "Global_Sales": "Global"
    }

    for key, region_name in regions.items():
        print(f"\n--- TOP 5 GAMES IN {region_name} ---")

        sorted_games = sorted(
            database,
            key=lambda g: g[key],
            reverse=True
        )
        top_five = sorted_games[:5]

        for i, game in enumerate(top_five, start=1):
            print(
                f"{i}. {game['Title']} ({game['Platform']}) — {game[key]} million units"
            )


# GUI-friendly version
def top_five_games_by_region_gui(database):
    """
    Return top 5 games per region for GUI.
    """
    regions = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Other_Sales": "Other Regions",
        "Global_Sales": "Global"
    }

    output = {}

    for key, region_name in regions.items():
        sorted_games = sorted(
            database,
            key=lambda g: g[key],
            reverse=True
        )
        output[region_name] = sorted_games[:5]

    return output


# CLI entry point
def run(database):
    top_five_games_by_region(database)
