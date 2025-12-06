#feature 3 : game recommendations

def print_rec(games):
    if not games:
        print("\nNo recommendations found, try another game.\n")
        return
    
    print("\n--- Game Recommendations ---")
    for game, score in games:
        print(
            f"{game['name']} | {game['platform']} | {game['genre']} | "
            f"Year: {game['year']} | Global Sales: {game['global_sales']}m | "
         
        )
    print("-----------------------------\n")

#------------------------
# main reccomendation logic
#------------------------

def rec_game(database, chosen_game):
    recommendations = []

    for game in database:
        # dont recommend the game itself
        if game["name"].lower() == chosen_game["name"].lower():
            continue
        score = 0

         # Match by GENRE (strong match)
        if game["genre"].lower() == chosen_game["genre"].lower():
            score += 2

        # Match by PLATFORM (medium match)
        if game["platform"].lower() == chosen_game["platform"].lower():
            score += 1

        # Match by SALES (small match)
        if abs(game["global_sales"] - chosen_game["global_sales"]) <= 1.0:
            score += 1

        # Only add games that got any score
        if score > 0:
            recommendations.append((game, score))

    # Sort by score (best matches first)
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Only return top 5
    return recommendations[:5]

#------------------------
# main feature runner
#------------------------

def run(database):
    print("\n=== Game Recommendation System ===")

    # ask user which game they want to base recommendations on
    chosen_name = input("Enter the name of a game you like: ").strip().lower()

    # try to find the game in the database
    chosen_game = None
    for game in database:
        if chosen_name == game["name"].lower():
            chosen_game = game
            break
    if chosen_game is None:
        print("Game not found in database.")
        return
    
    #build reccommendations
    results = rec_game(database, chosen_game)

    #print for user
    print_rec(results)
