# feature2.py — Search & Filtering System


# Print games to CLI
def print_games(games):
    """
    Prints a list of games in a readable CLI format.
    Shows top 5 by Global Sales.
    """
    if not games:
        print("No games found.")
        return

    print("\n--- Search Results ---")
    print("\n--- Top 5 by Global Sales ---\n")

    for game in games:
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )

    print("----------------------\n")


# GUI helper search
def search_games(database, keyword):
    """
    Search games by name for GUI.
    Returns top 5 matches by Global Sales.
    """
    keyword = keyword.strip().lower()

    results = [
        g for g in database
        if keyword in g["Title"].strip().lower()
    ]

    results = sorted(
        results,
        key=lambda g: g["Global_Sales"],
        reverse=True
    )[:5]

    return results


# CLI search by name
def search_by_name(database, preset_name=None):
    """
    Search games by name in CLI.
    """
    if preset_name:
        name = preset_name.strip().lower()
    else:
        name = input("Enter game name to search: ").strip().lower()

    results = [
        g for g in database
        if name in g['Title'].strip().lower()
    ]

    top5 = sorted(
        results,
        key=lambda g: g['Global_Sales'],
        reverse=True
    )[:5]

    print_games(top5)


# CLI search by platform
def search_by_platform(database):
    """Search games by platform in CLI."""
    platform = input("Enter platform: ").strip().lower()

    results = [
        g for g in database
        if g['Platform'].strip().lower() == platform
    ]

    top5 = sorted(
        results,
        key=lambda g: g['Global_Sales'],
        reverse=True
    )[:5]

    print_games(top5)


# CLI search by genre
def search_by_genre(database):
    """Search games by genre in CLI."""
    genre = input("Enter genre: ").strip().lower()

    results = [
        g for g in database
        if g['Genre'].strip().lower() == genre
    ]

    top5 = sorted(
        results,
        key=lambda g: g['Global_Sales'],
        reverse=True
    )[:5]

    print_games(top5)


# CLI search by publisher
def search_by_publisher(database):
    """Search games by publisher in CLI."""
    publisher = input("Enter publisher: ").strip().lower()

    results = [
        g for g in database
        if g['Publisher'].strip().lower() == publisher
    ]

    top5 = sorted(
        results,
        key=lambda g: g['Global_Sales'],
        reverse=True
    )[:5]

    print_games(top5)


# Filter games by year and sales
def filter_games(database):
    """
    Filter games by year range and minimum sales.
    """
    print("Enter year range for filtering.")

    try:
        start = int(input("Start year: "))
        end = int(input("End year: "))
        min_sales = float(input("Minimum global sales (in millions): "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    results = [
        g for g in database
        if g['Year_of_Release'] is not None
        and start <= g['Year_of_Release'] <= end
        and g['Global_Sales'] >= min_sales
    ]

    top5 = sorted(
        results,
        key=lambda g: g['Global_Sales'],
        reverse=True
    )[:5]

    print_games(top5)


# CLI menu
def run(database):
    """
    Main CLI menu for search and filtering.
    """
    while True:
        print("\n=== SEARCH & FILTER SYSTEM ===")
        print("1. Search by Name")
        print("2. Search by Platform")
        print("3. Search by Genre")
        print("4. Search by Publisher")
        print("5. Filter by Year + Min Sales")
        print("Q. Back to Menu")

        choice = input("Choose an option: ").strip().upper()

        if choice == "1":
            search_by_name(database)
        elif choice == "2":
            search_by_platform(database)
        elif choice == "3":
            search_by_genre(database)
        elif choice == "4":
            search_by_publisher(database)
        elif choice == "5":
            filter_games(database)
        elif choice == "Q":
            break
        else:
            search_by_name(database, preset_name=choice)
