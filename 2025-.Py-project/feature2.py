#feature 2: search & filtering

def print_games(games):
   if not games:
      print("no games found")
      return
   

   print("\n--- Search Results ---")
   for game in games:
      print(
         f"{game['name']} | {game['platform']} | {game['genre']} | "
            f"Year: {game['year']} | Global Sales: {game['global_sales']}m"
      )

print("----------------------\n")
    
def search_by_name(database):
   name = input("Enter game name to search: ").strip().lower()

   results = []
   for game in database:
      if name in game["name".lower()]:
         results.append(game)

   print_games(results)

def search_by_platform(database):
   platform = input("Enter platform: ").strip().lower()
   results = [g for g in database if g["platform"].lower() == platform]
   print_games(results)

def search_by_genre(database):
   genre = input("Enter genre: ").strip().lower()
   results = [g for g in database if g["genre"].lower() == genre]
   print_games(results)

def search_by_publisher(database):
   publisher = input("Enter publisher: ").strip().lower()
   results = [g for g in database if g["publisher"].lower() == publisher]
   print_games(results)


#------------------------
# filtering by year range and minimum global sales
#------------------------

def filter_games(database):
   print("Enter year range for filtering.")

   try:
      start = int(input("Start year: "))
      end = int(input("End year: "))
      min_sales = float(input("Minimum global sales (in millions): "))
   except ValueError:
      print("Invalid input. Please enter a number.")
      return

   results = []
   for game in database:
        if game["year"] is None:
              continue
           
        if start <= game["year"] <= end and game["global_sales"] >= min_sales:
           results.append(game)

   print_games(results)

# -----------------------------------------------------------
# Main Feature Runner
# -----------------------------------------------------------
def run(database):
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
    else:
        print("Returning to main menu...")



   
