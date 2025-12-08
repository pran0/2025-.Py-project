# feature3.py — Game Recommendations

def print_rec(games):
    if not games:
        print("\nNo recommendations found, try another game.\n")
        return

    print("\n--- Game Recommendations ---")
    for game, score in games:
        print(
            f"{game['Title']} | {game['Platform']} | {game['Genre']} | "
            f"Year: {game['Year_of_Release']} | Global Sales: {game['Global_Sales']}m"
        )
    print("-----------------------------\n")


# ------------------------
# main recommendation logic
# ------------------------

def rec_game(database, chosen_game):
    recommendations = []

    for game in database:
        # don't recommend the game itself
        if game["Title"].strip().lower() == chosen_game["Title"].strip().lower():
            continue

        score = 0

        # Match by GENRE (strong match)
        if game["Genre"].strip().lower() == chosen_game["Genre"].strip().lower():
            score += 2

        # Match by PLATFORM (medium match)
        if game["Platform"].strip().lower() == chosen_game["Platform"].strip().lower():
            score += 1

        # Match by SALES (small match, within 1 million)
        if abs(game["Global_Sales"] - chosen_game["Global_Sales"]) <= 1.0:
            score += 1

        # Only add games that got any score
        if score > 0:
            recommendations.append((game, score))

    # Sort by score (best matches first)
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Only return top 5 recommendations
    return recommendations[:5]


# ------------------------
# main feature runner
# ------------------------

def run(database):
    print("\n=== Game Recommendation System ===")

    chosen_name = input("Enter the name of a game you like: ").strip().lower()

    # try to find the game in the database
    chosen_game = None
    for game in database:
        if chosen_name == game["Title"].strip().lower():
            chosen_game = game
            break

    if chosen_game is None:
        print("Game not found in database.")
        return

    # build recommendations
    results = rec_game(database, chosen_game)

    # print for user
    print_rec(results)

