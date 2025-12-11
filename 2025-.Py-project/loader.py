# This line brings in the csv library so we can read CSV (comma-separated values) files
import csv

# This creates a function called init that takes a file_path as input
def init(file_path):
    """
    Loads and processes game data from the CSV file.
    Returns a list of game dictionaries.
    """
    # This creates an empty list where we'll store all our game information
    games = []

    # This opens the file at file_path for reading ('r'), using utf-8 encoding to handle special characters
    with open(file_path, 'r', encoding="utf-8") as file:
        # This creates a special reader that automatically reads each row as a dictionary
        reader = csv.DictReader(file)

        # This loops through each row in the CSV file one at a time
        for row in reader:
            # This starts a try block - it tries to run code that might cause an error
            try:
                # This creates a dictionary (like a mini database) for one game with all its information
                game = {
                    # This gets the game's name from the row and removes extra spaces
                    'Title': row['name'].strip(),                    # Game title
                    # This gets the gaming platform (like PS4 or Xbox) and removes extra spaces
                    'Platform': row['platform'].strip(),            # Platform (e.g., PS4, Xbox)
                    # This converts the year to a whole number, or sets it to None if the year is missing
                    'Year_of_Release': int(float(row['year'])) if row['year'] else None,
                    # This gets the game's genre (like Action or Sports) and removes extra spaces
                    'Genre': row['genre'].strip(),
                    # This gets the publisher's name (the company that made the game) and removes extra spaces
                    'Publisher': row['publisher'].strip(),
                    # This converts North America sales to a decimal number, or uses 0.0 if it's missing
                    'NA_Sales': float(row['na_sales']) if row['na_sales'] else 0.0,
                    # This converts Europe sales to a decimal number, or uses 0.0 if it's missing
                    'EU_Sales': float(row['eu_sales']) if row['eu_sales'] else 0.0,
                    # This converts Japan sales to a decimal number, or uses 0.0 if it's missing
                    'JP_Sales': float(row['jp_sales']) if row['jp_sales'] else 0.0,
                    # This converts other regions' sales to a decimal number, or uses 0.0 if it's missing
                    'Other_Sales': float(row['other_sales']) if row['other_sales'] else 0.0,
                    # This converts global (worldwide) sales to a decimal number, or uses 0.0 if it's missing
                    'Global_Sales': float(row['global_sales']) if row['global_sales'] else 0.0,
                }

                # This adds the game dictionary we just created to our list of all games
                games.append(game)

            # This catches errors that happen when we try to convert text to numbers but it's not a valid number
            except ValueError:
                # Skip any row that has invalid numbers
                # This skips this row and moves on to the next one without crashing
                continue

    # This sends back the complete list of all games we collected
    return games
