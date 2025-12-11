# feature2.py — Search & Filtering System

# This creates a function that prints a list of games in a nice format for the console
def print_games(games):
    """
    Prints a list of games in a readable format for CLI.
    Shows top 5 by Global Sales.
    """
    # This checks if there are no games to display
    if not games:
        # Inform user if no results
        # This tells the user no games were found
        print("No games found.")
        # This stops the function early since there's nothing to show
        return

    # This prints a header to show we're starting the search results
    print("\n--- Search Results ---")
    # This prints a sub-header explaining we're showing the top 5 by sales
    print("\n--- Top 5 by Global Sales ---\n")
    # This loops through each game in the list
    for game in games:
        # This prints all the important details about the game on one line
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )
    # This prints a footer line to show we're done with the results
    print("----------------------\n")


# ----------------------
# GUI HELPER FUNCTION
# ----------------------
# This creates a function that the graphical interface uses to search for games
def search_games(database, keyword):
    """
    Search for games by name for the GUI.
    Returns top 5 matches sorted by Global Sales.
    """
    # Normalize user input
    # This converts the keyword to lowercase and removes extra spaces so we can match better
    keyword = keyword.strip().lower()

    # Filter games containing the keyword
    # This searches through all games and finds ones where the title contains the keyword
    results = [g for g in database if keyword in g["Title"].strip().lower()]

    # Sort by Global Sales descending and take top 5
    # This sorts the games from highest to lowest sales and takes only the first 5
    results = sorted(results, key=lambda g: g["Global_Sales"], reverse=True)[:5]

    # This returns the list of top 5 matching games
    return results


# ----------------------
# CLI SEARCH FUNCTIONS
# ----------------------
# This creates a function to search games by their name in the console
def search_by_name(database, preset_name=None):
    """
    Search games by name in CLI.
    Optionally accepts a preset name instead of asking user input.
    """
    # This checks if a name was already provided
    if preset_name:
        # This uses the provided name and converts it to lowercase without extra spaces
        name = preset_name.strip().lower()
    # This runs if no name was provided
    else:
        # This asks the user to type a game name and converts it to lowercase without extra spaces
        name = input("Enter game name to search: ").strip().lower()

    # Find all games containing the search keyword
    # This searches through all games and finds ones where the title contains what the user typed
    results = [g for g in database if name in g['Title'].strip().lower()]

    # Take top 5 by Global Sales
    # This sorts the results by sales (highest first) and takes only the top 5
    top5 = sorted(results, key=lambda g: g['Global_Sales'], reverse=True)[:5]
    # Display results
    # This calls the print function to show the results in a nice format
    print_games(top5)


# This creates a function to search games by their platform in the console
def search_by_platform(database):
    """Search games by platform in CLI."""
    # This asks the user to type a platform name and converts it to lowercase without extra spaces
    platform = input("Enter platform: ").strip().lower()
    # This searches for games where the platform matches exactly what the user typed
    results = [g for g in database if g['Platform'].strip().lower() == platform]

    # This sorts the results by sales (highest first) and takes only the top 5
    top5 = sorted(results, key=lambda g: g['Global_Sales'], reverse=True)[:5]
    # This displays the top 5 results in a nice format
    print_games(top5)


# This creates a function to search games by their genre in the console
def search_by_genre(database):
    """Search games by genre in CLI."""
    # This asks the user to type a genre and converts it to lowercase without extra spaces
    genre = input("Enter genre: ").strip().lower()
    # This searches for games where the genre matches exactly what the user typed
    results = [g for g in database if g['Genre'].strip().lower() == genre]

    # This sorts the results by sales (highest first) and takes only the top 5
    top5 = sorted(results, key=lambda g: g['Global_Sales'], reverse=True)[:5]
    # This displays the top 5 results in a nice format
    print_games(top5)


# This creates a function to search games by their publisher in the console
def search_by_publisher(database):
    """Search games by publisher in CLI."""
    # This asks the user to type a publisher name and converts it to lowercase without extra spaces
    publisher = input("Enter publisher: ").strip().lower()
    # This searches for games where the publisher matches exactly what the user typed
    results = [g for g in database if g['Publisher'].strip().lower() == publisher]

    # This sorts the results by sales (highest first) and takes only the top 5
    top5 = sorted(results, key=lambda g: g['Global_Sales'], reverse=True)[:5]
    # This displays the top 5 results in a nice format
    print_games(top5)


# ----------------------
# FILTER FUNCTION
# ----------------------
# This creates a function to filter games by year range and minimum sales
def filter_games(database):
    """
    Filters games by year range and minimum global sales.
    Prompts user for start year, end year, and minimum sales.
    """
    # This prints instructions for the user
    print("Enter year range for filtering.")

    # This starts a try block to catch errors if the user types something wrong
    try:
        # This asks the user for the starting year and converts it to a whole number
        start = int(input("Start year: "))
        # This asks the user for the ending year and converts it to a whole number
        end = int(input("End year: "))
        # This asks the user for minimum sales and converts it to a decimal number
        min_sales = float(input("Minimum global sales (in millions): "))
    # This catches errors when the user types something that's not a number
    except ValueError:
        # Handle invalid input
        # This tells the user they need to enter valid numbers
        print("Invalid input. Please enter numbers only.")
        # This stops the function early
        return

    # Filter games meeting year and sales criteria
    # This searches for games that were released between the start and end years AND have sales above the minimum
    results = [
        g for g in database
        if g['Year_of_Release'] is not None and start <= g['Year_of_Release'] <= end
        and g['Global_Sales'] >= min_sales
    ]

    # Take top 5 by Global Sales
    # This sorts the filtered results by sales (highest first) and takes only the top 5
    top5 = sorted(results, key=lambda g: g['Global_Sales'], reverse=True)[:5]
    # This displays the top 5 results in a nice format
    print_games(top5)


# ----------------------
# CLI MENU
# ----------------------
# This creates the main menu function for the search system in the console
def run(database):
    """
    Main CLI menu for search and filtering system.
    Allows user to choose search/filter options or quit.
    """
    # This starts a loop that keeps running until the user chooses to quit
    while True:
        # This prints a header for the search menu
        print("\n=== SEARCH & FILTER SYSTEM ===")
        # This prints the first menu option
        print("1. Search by Name")
        # This prints the second menu option
        print("2. Search by Platform")
        # This prints the third menu option
        print("3. Search by Genre")
        # This prints the fourth menu option
        print("4. Search by Publisher")
        # This prints the fifth menu option
        print("5. Filter by Year + Min Sales")
        # This prints the quit option
        print("Q. Back to Menu")

        # Read user input
        # This asks the user to choose an option, removes extra spaces, and converts to uppercase
        choice = input("Choose an option: ").strip().upper()

        # This checks if the user typed "1"
        if choice == "1":
            # This runs the search by name function
            search_by_name(database)
        # This checks if the user typed "2"
        elif choice == "2":
            # This runs the search by platform function
            search_by_platform(database)
        # This checks if the user typed "3"
        elif choice == "3":
            # This runs the search by genre function
            search_by_genre(database)
        # This checks if the user typed "4"
        elif choice == "4":
            # This runs the search by publisher function
            search_by_publisher(database)
        # This checks if the user typed "5"
        elif choice == "5":
            # This runs the filter by year and sales function
            filter_games(database)
        # This checks if the user typed "Q"
        elif choice == "Q":
            # Exit CLI menu
            # This breaks out of the loop and goes back to the main menu
            break
        # This runs if the user typed anything else
        else:
            # If input is invalid, treat it as a name search
            # This assumes the user typed a game name and searches for it
            search_by_name(database, preset_name=choice)
