# main.py

import csv                       # Import the CSV module to read CSV files
from config import file_path     # Import the file path of the game dataset from config.py
from gui import GameApp          # Import the GUI class for launching the application
import features.feature2 as feature2   # Import Feature 2 (search functionality)
import features.feature3 as feature3   # Import Feature 3 (recommendation system)


def init(file_path):
    """
    Loads and processes game data from the CSV file.
    Returns a list of game dictionaries.
    """
    games = []  # List that will store each game as a dictionary

    # Open the CSV file using UTF-8 encoding
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Reads rows as dictionaries using column headers

        # Loop through each row in the CSV file
        for row in reader:
            try:
                # Create a dictionary for each game with cleaned and converted values
                game = {
                    'Title': row['name'].strip(),  # Game title
                    'Platform': row['platform'].strip(),  # Platform (e.g., PS4, Xbox)
                    'Year_of_Release': int(float(row['year'])) if row['year'] else None,
                    # Convert year to int if it exists
                    'Genre': row['genre'].strip(),  # Genre of the game
                    'Publisher': row['publisher'].strip(),  # Publisher name
                    'NA_Sales': float(row['na_sales']) if row['na_sales'] else 0.0,
                    'EU_Sales': float(row['eu_sales']) if row['eu_sales'] else 0.0,
                    'JP_Sales': float(row['jp_sales']) if row['jp_sales'] else 0.0,
                    'Other_Sales': float(row['other_sales']) if row['other_sales'] else 0.0,
                    'Global_Sales': float(row['global_sales']) if row['global_sales'] else 0.0,
                    # Convert sales values to floats, defaulting to 0.0
                }

                games.append(game)  # Add the processed game to the list

            except ValueError:
                # Skip any row that has invalid data types
                continue

    return games  # Return the full game list


def main():
    """
    Main console application loop (not used when GUI is running).
    Allows user to choose features from the terminal.
    """
    print("Loading game data...")

    try:
        database = init(file_path)  # Load game database from CSV
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")  # Handle missing file
        return

    print(f"Loaded {len(database)} games.")  # Show how many games were loaded

    # Infinite loop for the console menu
    while True:
        print("\n1. Feature 2 (Search)")
        print("2. Feature 3 (Recommendations)")
        print("3. Exit")

        choice = input("Choose an option: ").strip()  # Read user input

        if choice == "1":
            feature2.run(database)  # Run search feature

        elif choice == "2":
            feature3.run(database)  # Run recommendation feature

        elif choice == "3":
            print("Goodbye!")  # Exit program
            break

        else:
            print("Invalid choice.")  # Handle incorrect menu selection


# If this file is run directly (not imported), start the GUI application
if __name__ == "__main__":
    app = GameApp()     # Create GUI app instance
    app.mainloop()      # Start the event loop (opens the GUI window)
