# feature2.py — Search & Filtering System

def print_games(games):
    if not games:
        print("No games found.")
        return

    print("\n--- Search Results ---")
    for game in games:
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )
    print("----------------------\n")


# ----------------------
# SEARCH FUNCTIONS
# ----------------------

def search_by_name(database, preset_name=None):
    if preset_name:
        name = preset_name.strip().lower()
    else:
        name = input("Enter game name to search: ").strip().lower()

    results = [g for g in database if name in g['Title'].strip().lower()]

    print_games(results)


def search_by_platform(database):
    platform = input("Enter platform: ").strip().lower()
    results = [g for g in database if g['Platform'].strip().lower() == platform]
    print_games(results)


def search_by_genre(database):
    genre = input("Enter genre: ").strip().lower()
    results = [g for g in database if g['Genre'].strip().lower() == genre]
    print_games(results)


def search_by_publisher(database):
    publisher = input("Enter publisher: ").strip().lower()
    results = [g for g in database if g['Publisher'].strip().lower() == publisher]
    print_games(results)


# ----------------------
# FILTERING (YEAR + MIN SALES)
# ----------------------

def filter_games(database):
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
        if g['Year_of_Release'] is not None and start <= g['Year_of_Release'] <= end
        and g['Global_Sales'] >= min_sales
    ]

    print_games(results)


# ----------------------
# FEATURE 2 MENU
# ----------------------

def run(database):
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
            # If user types a game name directly, search it
            search_by_name(database, preset_name=choice)
