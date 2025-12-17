# feature3.py — Game Recommendations


# Print recommendations to CLI
def print_rec(games):
    """
    Prints game recommendations for CLI.
    """
    if not games:
        print("\nNo recommendations found.\n")
        return

    print("\n--- Game Recommendations ---")

    for game, score in games:
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )

    print("-----------------------------\n")


# Core recommendation logic
def rec_game(database, chosen_game):
    """
    Compare a chosen game against others and return top recommendations.
    """
    recommendations = []

    for game in database:
        if game["Title"].strip().lower() == chosen_game["Title"].strip().lower():
            continue

        score = 0

        if game["Genre"].strip().lower() == chosen_game["Genre"].strip().lower():
            score += 2

        if game["Platform"].strip().lower() == chosen_game["Platform"].strip().lower():
            score += 1

        if abs(game["Global_Sales"] - chosen_game["Global_Sales"]) <= 1.0:
            score += 1

        if score > 0:
            recommendations.append((game, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:5]


# GUI helper
def recommend_games(database, title):
    """
    Return recommended games for GUI.
    """
    title = title.strip().lower()

    matches = [
        g for g in database
        if title in g["Title"].strip().lower()
    ]

    if not matches:
        return []

    chosen = matches[0]
    recs = rec_game(database, chosen)

    return [g for g, score in recs]


# CLI entry point
def run(database):
    """
    CLI interface for recommendations.
    """
    print("\n=== Game Recommendation System ===")

    chosen_name = input("Enter game name: ").strip().lower()

    matches = [
        g for g in database
        if chosen_name in g["Title"].strip().lower()
    ]

    if not matches:
        print("Game not found.")
        return

    chosen_game = matches[0]
    results = rec_game(database, chosen_game)

    print_rec(results)
