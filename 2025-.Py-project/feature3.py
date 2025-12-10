# feature3.py — Game Recommendations

def print_rec(games):
    """
    Prints game recommendations in a readable format for CLI.
    Each game is displayed with its main details and global sales.
    """
    if not games:
        print("\nNo recommendations found.\n")  # Inform user if no recommendations
        return

    print("\n--- Game Recommendations ---")
    for game, score in games:  # Iterate over recommended games (with their scores)
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )
    print("-----------------------------\n")


# ------------------------
# MAIN LOGIC
# ------------------------
def rec_game(database, chosen_game):
    """
    Core recommendation algorithm.
    Compares chosen game with others in the database and assigns a similarity score.
    Returns top 5 recommendations.
    """
    recommendations = []  # List to store potential recommendations along with their scores

    for game in database:
        # Skip the chosen game itself
        if game["Title"].strip().lower() == chosen_game["Title"].strip().lower():
            continue

        score = 0  # Initialize similarity score

        # Add points if genre matches
        if game["Genre"].strip().lower() == chosen_game["Genre"].strip().lower():
            score += 2

        # Add points if platform matches
        if game["Platform"].strip().lower() == chosen_game["Platform"].strip().lower():
            score += 1

        # Add points if global sales are similar (within 1 million)
        if abs(game["Global_Sales"] - chosen_game["Global_Sales"]) <= 1.0:
            score += 1

        # Only consider games with at least 1 point
        if score > 0:
            recommendations.append((game, score))

    # Sort recommendations by score in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Return top 5 recommendations
    return recommendations[:5]


# ------------------------
# GUI HELPER FUNCTION
# ------------------------
def recommend_games(database, title):
    """
    Helper function for the GUI.
    Finds a game by title and returns a list of recommended game dictionaries.
    """
    title = title.strip().lower()  # Normalize input for matching

    # Find all games containing the input keyword
    matches = [g for g in database if title in g["Title"].strip().lower()]

    if not matches:
        return []  # No matches found

    chosen = matches[0]  # Take the first match

    recs = rec_game(database, chosen)  # Get recommendations

    # GUI only needs the game dictionaries (without scores)
    return [g for g, score in recs]


# ------------------------
# CLI VERSION
# ------------------------
def run(database):
    """
    Command-line interface for game recommendations.
    Prompts user for a game and prints top recommendations.
    """
    print("\n=== Game Recommendation System ===")

    # Ask user for the game name
    chosen_name = input("Enter game name: ").strip().lower()

    # Find matches in the database
    matches = [g for g in database if chosen_name in g["Title"].strip().lower()]

    if not matches:
        print("Game not found.")  # Inform user if no matches
        return

    chosen_game = matches[0]  # Select the first match

    results = rec_game(database, chosen_game)  # Generate recommendations

    print_rec(results)  # Print recommendations to console
# ------------------------
