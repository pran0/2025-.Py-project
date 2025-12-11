# gui.py
# This line brings in the tkinter library so we can create windows and buttons
import tkinter as tk
# This line brings in special tkinter widgets (like tabs and styled buttons) and message boxes
from tkinter import ttk, messagebox

# This line brings in the code from feature1.py so we can use it here
import features.feature1 as feature1
# This line brings in the code from feature2.py so we can use it here
import features.feature2 as feature2
# This line brings in the code from feature3.py so we can use it here
import features.feature3 as feature3
# This line brings in the code from feature4.py so we can use it here
import features.feature4 as feature4

# This line gets the init function from loader.py to load our game data
from loader import init
# This line gets the file_path variable from config.py which tells us where the data file is
from config import file_path


# This creates a new class (like a blueprint) for our game app window that inherits from tk.Tk
class GameApp(tk.Tk):
    # This is the special function that runs when we create a new GameApp
    def __init__(self):
        # This calls the parent class's __init__ to set up the basic window
        super().__init__()

        # This sets the title text that appears at the top of the window
        self.title("Game Database System")
        # This sets the size of the window to 950 pixels wide and 650 pixels tall
        self.geometry("950x650")

        # Load processed game data once.
        # This loads all the game data from the file and stores it in self.data so we can use it
        self.data = init(file_path)

        # This creates a notebook widget which is like a folder with tabs
        notebook = ttk.Notebook(self)
        # This makes the notebook fill the entire window and expand if the window gets bigger
        notebook.pack(expand=True, fill="both")

        # Create tabs
        # This creates a frame (like a blank canvas) for the first feature tab
        self.tab_feature1 = ttk.Frame(notebook)
        # This creates a frame for the second feature tab
        self.tab_feature2 = ttk.Frame(notebook)
        # This creates a frame for the third feature tab
        self.tab_feature3 = ttk.Frame(notebook)
        # This creates a frame for the fourth feature tab
        self.tab_feature4 = ttk.Frame(notebook)

        # This adds the first tab to the notebook and labels it "Sales Analysis"
        notebook.add(self.tab_feature1, text="Sales Analysis")
        # This adds the second tab to the notebook and labels it "Search"
        notebook.add(self.tab_feature2, text="Search")
        # This adds the third tab to the notebook and labels it "Recommendations"
        notebook.add(self.tab_feature3, text="Recommendations")
        # This adds the fourth tab to the notebook and labels it "Top 5 Leaderboards"
        notebook.add(self.tab_feature4, text="Top 5 Leaderboards")

        # Build tab UIs
        # This calls the function to create all the buttons and text boxes for feature 1
        self.build_feature1_tab()
        # This calls the function to create all the buttons and text boxes for feature 2
        self.build_feature2_tab()
        # This calls the function to create all the buttons and text boxes for feature 3
        self.build_feature3_tab()
        # This calls the function to create all the buttons and text boxes for feature 4
        self.build_feature4_tab()

    # --------------------------------------
    # FEATURE 1 GUI (Sales Analysis)
    # --------------------------------------
    # This function builds the interface for the first feature tab
    def build_feature1_tab(self):
        # This stores the feature 1 tab frame in a variable so it's easier to use
        frame = self.tab_feature1

        # This creates a text label asking the user to enter a game title and adds some space around it
        tk.Label(frame, text="Enter game title for sales analysis:").pack(pady=10)

        # This creates a text entry box that's 40 characters wide where users can type
        self.f1_entry = tk.Entry(frame, width=40)
        # This adds the entry box to the window
        self.f1_entry.pack()

        # This creates a button labeled "Generate Chart" that runs do_feature1 when clicked
        tk.Button(frame, text="Generate Chart",
                  command=self.do_feature1).pack(pady=10)

    # This function runs when the user clicks the "Generate Chart" button
    def do_feature1(self):
        # This gets the text the user typed in the entry box and removes extra spaces
        game_name = self.f1_entry.get().strip()

        # This checks if the user didn't type anything
        if not game_name:
            # This shows a warning pop-up message telling the user to enter a game title
            messagebox.showwarning("Missing Input", "Enter a game title.")
            # This stops the function early since we don't have a game name
            return

        # This runs the feature1 function with our data and the game name, and stores whether it worked
        success = feature1.run_gui_feature1(self.data, game_name)

        # This checks if the function didn't find the game
        if not success:
            # This shows an error pop-up message saying the game wasn't found
            messagebox.showerror("Not Found",
                                 f"No sales data found for '{game_name}'")

    # --------------------------------------
    # FEATURE 2 GUI (Search)
    # --------------------------------------
    # This function builds the interface for the second feature tab
    def build_feature2_tab(self):
        # This stores the feature 2 tab frame in a variable so it's easier to use
        frame = self.tab_feature2

        # This creates a text label asking the user to enter a search keyword and adds some space around it
        tk.Label(frame, text="Enter search keyword:").pack(pady=10)

        # This creates a text entry box that's 40 characters wide where users can type their search
        self.f2_entry = tk.Entry(frame, width=40)
        # This adds the entry box to the window
        self.f2_entry.pack()

        # This creates a button labeled "Search" that runs do_search when clicked
        tk.Button(frame, text="Search", command=self.do_search).pack(pady=10)

        # This creates a text box that's 22 lines tall where we'll show the search results
        self.f2_output = tk.Text(frame, height=22)
        # This adds the text box to the window and makes it fill all available space
        self.f2_output.pack(fill="both", expand=True)

    # This function runs when the user clicks the "Search" button
    def do_search(self):
        # This gets the search keyword the user typed and removes extra spaces
        keyword = self.f2_entry.get().strip()

        # This calls the search_games function to find games matching the keyword
        results = feature2.search_games(self.data, keyword)

        # This deletes everything currently in the output text box to start fresh
        self.f2_output.delete("1.0", tk.END)

        # This checks if no games were found
        if not results:
            # This writes "No results found." in the output text box
            self.f2_output.insert(tk.END, "No results found.")
            # This stops the function since there's nothing more to show
            return

        # This loops through each game that was found
        for g in results:
            # This writes the game's title, platform, and genre on a new line in the text box
            self.f2_output.insert(
                tk.END,
                f"{g['Title']} | {g['Platform']} | {g['Genre']}\n"
            )

    # --------------------------------------
    # FEATURE 3 GUI (Recommendations)
    # --------------------------------------
    # This function builds the interface for the third feature tab
    def build_feature3_tab(self):
        # This stores the feature 3 tab frame in a variable so it's easier to use
        frame = self.tab_feature3

        # This creates a text label asking the user to enter a game title and adds some space around it
        tk.Label(frame, text="Enter a game title:").pack(pady=10)

        # This creates a text entry box that's 40 characters wide where users can type a game name
        self.f3_entry = tk.Entry(frame, width=40)
        # This adds the entry box to the window
        self.f3_entry.pack()

        # This creates a button labeled "Get Recommendations" that runs do_feature3 when clicked
        tk.Button(frame, text="Get Recommendations",
                  command=self.do_feature3).pack(pady=10)

        # This creates a text box that's 22 lines tall where we'll show the recommended games
        self.f3_output = tk.Text(frame, height=22)
        # This adds the text box to the window and makes it fill all available space
        self.f3_output.pack(fill="both", expand=True)

    # This function runs when the user clicks the "Get Recommendations" button
    def do_feature3(self):
        # This gets the game title the user typed and removes extra spaces
        title = self.f3_entry.get().strip()

        # This calls the recommend_games function to find similar games
        results = feature3.recommend_games(self.data, title)

        # This deletes everything currently in the output text box to start fresh
        self.f3_output.delete("1.0", tk.END)

        # This checks if no recommendations were found
        if not results:
            # This writes "No recommendations available." in the output text box
            self.f3_output.insert(tk.END, "No recommendations available.")
            # This stops the function since there's nothing more to show
            return

        # This loops through each recommended game
        for g in results:
            # This writes the game's title, platform, and genre on a new line in the text box
            self.f3_output.insert(
                tk.END,
                f"{g['Title']} | {g['Platform']} | {g['Genre']}\n"
            )

    # --------------------------------------
    # FEATURE 4 GUI (Top 5 Leaderboards)
    # --------------------------------------
    # This function builds the interface for the fourth feature tab
    def build_feature4_tab(self):
        # This stores the feature 4 tab frame in a variable so it's easier to use
        frame = self.tab_feature4

        # This creates a large heading label with Arial font size 16 and adds some space around it
        tk.Label(
            frame,
            text="Top 5 Games by Region",
            font=("Arial", 16)
        ).pack(pady=10)

        # This creates a button labeled "Show Leaderboards" that runs do_feature4 when clicked
        tk.Button(
            frame,
            text="Show Leaderboards",
            command=self.do_feature4
        ).pack(pady=10)

        # This creates a text box that's 25 lines tall where we'll show the top games for each region
        self.f4_output = tk.Text(frame, height=25)
        # This adds the text box to the window and makes it fill all available space
        self.f4_output.pack(fill="both", expand=True)

    # This function runs when the user clicks the "Show Leaderboards" button
    def do_feature4(self):
        # This calls the function to get the top 5 games for each region
        results = feature4.top_five_games_by_region_gui(self.data)

        # This deletes everything currently in the output text box to start fresh
        self.f4_output.delete("1.0", tk.END)

        # This loops through each region and its top games
        for region, games in results.items():
            # This writes the region name as a heading with === marks around it
            self.f4_output.insert(tk.END, f"\n=== {region} ===\n")

            # This loops through each game in this region's top 5, numbering them starting from 1
            for i, g in enumerate(games, start=1):
                # This writes the rank number, game title, platform, and sales in millions
                self.f4_output.insert(
                    tk.END,
                    f"{i}. {g['Title']} ({g['Platform']}) — {g['Global_Sales']}m\n"
                )
