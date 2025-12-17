# feature3.py — Game Recommendations

# This creates a function that prints game recommendations in a nice format for the console
def print_rec(games):
    """
    Prints game recommendations in a readable format for CLI.
    Each game is displayed with its main details and global sales.
    """
    # This checks if there are no games to recommend
    if not games:
        # Inform user if no recommendations
        # This prints a message telling the user no recommendations were found
        print("\nNo recommendations found.\n")
        # This stops the function early since there's nothing to show
        return

    # This prints a header to show we're starting the recommendations section
    print("\n--- Game Recommendations ---")
    # Iterate over recommended games (with their scores)
    # This loops through each game and its similarity score
    for game, score in games:
        # This prints all the important details about the game on one line
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )
    # This prints a footer line to show we're done with recommendations
    print("-----------------------------\n")


# ------------------------
# MAIN LOGIC
# ------------------------
# This creates the main function that figures out which games are similar
def rec_game(database, chosen_game):
    """
    Core recommendation algorithm.
    Compares chosen game with others in the database and assigns a similarity score.
    Returns top 5 recommendations.
    """
    # List to store potential recommendations along with their scores
    # This creates an empty list where we'll store games and their similarity scores
    recommendations = []

    # This loops through every game in our database
    for game in database:
        # Skip the chosen game itself
        # This checks if this game is the same as the one we're comparing to
        if game["Title"].strip().lower() == chosen_game["Title"].strip().lower():
            # This skips this game and moves to the next one
            continue

        # Initialize similarity score
        # This starts the similarity score at 0 for this game
        score = 0

        # Add points if genre matches
        # This checks if this game has the same genre as the chosen game
        if game["Genre"].strip().lower() == chosen_game["Genre"].strip().lower():
            # This adds 2 points to the score because the genres match
            score += 2

        # Add points if platform matches
        # This checks if this game is on the same platform as the chosen game
        if game["Platform"].strip().lower() == chosen_game["Platform"].strip().lower():
            # This adds 1 point to the score because the platforms match
            score += 1

        # Add points if global sales are similar (within 1 million)
        # This checks if the sales numbers are close to each other (difference is 1 million or less)
        if abs(game["Global_Sales"] - chosen_game["Global_Sales"]) <= 1.0:
            # This adds 1 point to the score because they have similar popularity
            score += 1

        # Only consider games with at least 1 point
        # This checks if the game got any points at all
        if score > 0:
            # This adds the game and its score to our recommendations list
            recommendations.append((game, score))

    # Sort recommendations by score in descending order
    # This sorts all recommendations from highest score to lowest score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Return top 5 recommendations
    # This returns only the first 5 games from our sorted list (the best matches)
    return recommendations[:5]


# ------------------------
# GUI HELPER FUNCTION
# ------------------------
# This creates a helper function that the graphical interface uses
def recommend_games(database, title):
    """
    Helper function for the GUI.
    Finds a game by title and returns a list of recommended game dictionaries.
    """
    # Normalize input for matching
    # This converts the title to lowercase and removes extra spaces so we can match it better
    title = title.strip().lower()

    # Find all games containing the input keyword
    # This searches through all games and finds ones where the title contains what the user typed
    matches = [g for g in database if title in g["Title"].strip().lower()]

    # This checks if we didn't find any matching games
    if not matches:
        # No matches found
        # This returns an empty list since we have nothing to recommend
        return []

    # Take the first match
    # This picks the first game from the matches we found
    chosen = matches[0]

    # Get recommendations
    # This calls our main recommendation function to find similar games
    recs = rec_game(database, chosen)

    # GUI only needs the game dictionaries (without scores)
    # This extracts just the game information (not the scores) and returns it as a list
    return [g for g, score in recs]


# ------------------------
# CLI VERSION
# ------------------------
# This creates a function that runs the recommendation system in the console
def run(database):
    """
    Command-line interface for game recommendations.
    Prompts user for a game and prints top recommendations.
    """
    # This prints a header for the recommendation system
    print("\n=== Game Recommendation System ===")

    # Ask user for the game name
    # This asks the user to type a game name and converts it to lowercase without extra spaces
    chosen_name = input("Enter game name: ").strip().lower()

    # Find matches in the database
    # This searches through all games to find ones where the name contains what the user typed
    matches = [g for g in database if chosen_name in g["Title"].strip().lower()]

    # This checks if we didn't find any matching games
    if not matches:
        # Inform user if no matches
        # This tells the user the game wasn't found
        print("Game not found.")
        # This stops the function early
        return

    # Select the first match
    # This picks the first game from the matches we found
    chosen_game = matches[0]

    # Generate recommendations
    # This calls our main function to find games similar to the chosen one
    results = rec_game(database, chosen_game)

    # Print recommendations to console
    # This displays all the recommended games in a nice format
    print_rec(results)
# ------------------------
