# feature4.py — Top 5 Games by Region Leaderboards

def top_five_games_by_region(database):
    """
    Prints top 5 games for each region (console version).
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

        sorted_games = sorted(database, key=lambda g: g[key], reverse=True)
        top_five = sorted_games[:5]

        for i, game in enumerate(top_five, start=1):
            print(f"{i}. {game['Title']} ({game['Platform']}) — {game[key]} million units")


def top_five_games_by_region_gui(database):
    """
    GUI-friendly version.
    Returns a dict:
    {
        'North America': [(game, value), ...],
        'Europe': [...],
        ...
    }
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
        sorted_games = sorted(database, key=lambda g: g[key], reverse=True)
        top_five = sorted_games[:5]
        output[region_name] = top_five

    return output


# Console runner (optional)
def run(database):
    top_five_games_by_region(database)
