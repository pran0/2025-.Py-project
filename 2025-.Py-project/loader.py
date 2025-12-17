# Import CSV library
import csv


# Load game data from a CSV file
def init(file_path):
    """
    Loads and processes game data from the CSV file.
    Returns a list of game dictionaries.
    """
    # Store all games
    games = []

    # Open the CSV file
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Process each row
        for row in reader:
            try:
                # Create a game record
                game = {
                    'Title': row['name'].strip(),
                    'Platform': row['platform'].strip(),
                    'Year_of_Release': int(float(row['year'])) if row['year'] else None,
                    'Genre': row['genre'].strip(),
                    'Publisher': row['publisher'].strip(),
                    'NA_Sales': float(row['na_sales']) if row['na_sales'] else 0.0,
                    'EU_Sales': float(row['eu_sales']) if row['eu_sales'] else 0.0,
                    'JP_Sales': float(row['jp_sales']) if row['jp_sales'] else 0.0,
                    'Other_Sales': float(row['other_sales']) if row['other_sales'] else 0.0,
                    'Global_Sales': float(row['global_sales']) if row['global_sales'] else 0.0,
                }

                # Add game to list
                games.append(game)

            except ValueError:
                # Skip invalid rows
                continue

    # Return all games
    return games
