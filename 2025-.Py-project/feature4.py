def top_five_games_by_region(database):
    regions = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Other_Sales": "Other Regions",
        "Global_Sales": "Global"
    }

    for key, region_name in regions.items():
        print(f"\n--- TOP 5 GAMES IN {region_name} ---")

        sorted_games = sorted(database, key=lambda g: g[key], reverse=True)
        top_five = sorted_games[:5]

        for game in top_five:
            print(f"{game['Title']} — {game[key]} million")
