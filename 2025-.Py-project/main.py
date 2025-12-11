# This line brings in the code from feature1.py so we can use it here
import features.feature1 as feature1

# This line brings in the code from feature2.py so we can use it here
import features.feature2 as feature2

# This line brings in the code from feature3.py so we can use it here
import features.feature3 as feature3

# This line brings in the code from feature4.py so we can use it here
import features.feature4 as feature4

# This line gets the file_path variable from the config.py file
from config import file_path

# This line gets the init function from the loader.py file (moved from gui.py import)
from loader import init             # moved from gui.py import

# This line gets the GameApp class from the gui.py file
from gui import GameApp


# This creates a function called main that will run our program
def main():
    # This prints a message to tell the user we're starting to load the game data
    print("Loading game data...")

    # This starts a try block - it tries to run code that might cause an error
    try:
        # This calls the init function with the file_path to load all the game data into a variable called database
        database = init(file_path)
    # This catches the error if the file doesn't exist on the computer
    except FileNotFoundError:
        # This prints an error message telling the user which file couldn't be found
        print(f"Error: File '{file_path}' not found.")
        # This stops the function and exits the program early
        return

    # This prints how many games were loaded by counting the items in database
    print(f"Loaded {len(database)} games.")

    # This starts a loop that will keep running forever until we tell it to stop
    while True:
        # This prints a blank line to make the menu easier to read
        print("\n1. Feature 2 (Search)")
        # This prints the first menu option for searching games
        print("2. Feature 3 (Recommendations)")
        # This prints the second menu option for getting game recommendations
        print("3. Feature 4 (Top 5 Games by Region)")
        # This prints the third menu option for seeing top games by region
        print("4. Exit")
        # This prints the fourth menu option to quit the program

        # This asks the user to type a number and removes any extra spaces from their answer
        choice = input("Choose an option: ").strip()

        # This checks if the user typed "1"
        if choice == "1":
            # This runs the search feature using the database
            feature2.run(database)

        # This checks if the user typed "2" instead
        elif choice == "2":
            # This runs the recommendations feature using the database
            feature3.run(database)

        # This checks if the user typed "3" instead
        elif choice == "3":
            # This runs the top 5 games by region feature using the database
            feature4.run(database)

        # This checks if the user typed "4" instead
        elif choice == "4":
            # This prints a goodbye message to the user
            print("Goodbye!")
            # This breaks out of the loop and stops the program
            break
        # This runs if the user typed anything else that wasn't 1, 2, 3, or 4
        else:
            # This tells the user their choice wasn't valid
            print("Invalid choice.")


# This checks if this file is being run directly (not imported into another file)
if __name__ == "__main__":
    # This creates a new GameApp object which starts the graphical window
    app = GameApp()
    # This starts the main loop that keeps the window open and running
    app.mainloop()
