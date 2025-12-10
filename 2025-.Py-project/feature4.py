def top_five_games_by_region(database):
    # Mapping of sales keys to readable region names
    regions = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Other_Sales": "Other Regions",
        "Global_Sales": "Global"
    }

    # Process each region
    for key, region_name in regions.items():
        print(f"\n--- TOP 5 GAMES IN {region_name} ---")

        # Sort games by sales in the selected region (highest first)
        sorted_games = sorted(database, key=lambda g: g[key], reverse=True)

        # Take the first five entries
        top_five = sorted_games[:5]

        # Print results
        for i, game in enumerate(top_five, start=1):
            print(f"{i}. {game['Title']} ({game['Platform']}) — {game[key]} million units")
