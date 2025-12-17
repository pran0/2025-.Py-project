# feature4.py — Top 5 Games by Region Leaderboards

# This creates a function that shows the top 5 games for each region in the console/terminal
def top_five_games_by_region(database):
    """
    Prints top 5 games for each region (console version).
    """
    # This creates a dictionary that matches sales column names to friendly region names
    regions = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Other_Sales": "Other Regions",
        "Global_Sales": "Global"
    }

    # This loops through each region in our dictionary
    for key, region_name in regions.items():
        # This prints a header showing which region we're looking at
        print(f"\n--- TOP 5 GAMES IN {region_name} ---")

        # This sorts all games by their sales in this region, from highest to lowest
        sorted_games = sorted(database, key=lambda g: g[key], reverse=True)
        # This takes only the first 5 games from the sorted list (the top 5)
        top_five = sorted_games[:5]

        # This loops through each of the top 5 games, numbering them starting from 1
        for i, game in enumerate(top_five, start=1):
            # This prints the rank number, game title, platform, and how many millions it sold
            print(f"{i}. {game['Title']} ({game['Platform']}) — {game[key]} million units")


# This creates a function that returns the top 5 games for the graphical interface
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
    # This creates a dictionary that matches sales column names to friendly region names
    regions = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Other_Sales": "Other Regions",
        "Global_Sales": "Global"
    }

    # This creates an empty dictionary where we'll store the top games for each region
    output = {}

    # This loops through each region in our dictionary
    for key, region_name in regions.items():
        # This sorts all games by their sales in this region, from highest to lowest
        sorted_games = sorted(database, key=lambda g: g[key], reverse=True)
        # This takes only the first 5 games from the sorted list (the top 5)
        top_five = sorted_games[:5]
        # This stores the top 5 games for this region in our output dictionary
        output[region_name] = top_five

    # This sends back the dictionary with all regions and their top 5 games
    return output


# Console runner (optional)
# This creates a function that runs the console version of feature 4
def run(database):
    # This calls the function to display the top 5 games in the console
    top_five_games_by_region(database)
