# gui.py
# Import GUI libraries
import tkinter as tk
from tkinter import ttk, messagebox

# Import feature modules
import features.feature1 as feature1
import features.feature2 as feature2
import features.feature3 as feature3
import features.feature4 as feature4

# Import data loader and config
from loader import init
from config import file_path


# Main application window
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Game Database System")
        self.geometry("950x650")

        # Load data
        self.data = init(file_path)

        # Create tab container
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Create tabs
        self.tab_feature1 = ttk.Frame(notebook)
        self.tab_feature2 = ttk.Frame(notebook)
        self.tab_feature3 = ttk.Frame(notebook)
        self.tab_feature4 = ttk.Frame(notebook)

        notebook.add(self.tab_feature1, text="Sales Analysis")
        notebook.add(self.tab_feature2, text="Search")
        notebook.add(self.tab_feature3, text="Recommendations")
        notebook.add(self.tab_feature4, text="Top 5 Leaderboards")

        # Build tabs
        self.build_feature1_tab()
        self.build_feature2_tab()
        self.build_feature3_tab()
        self.build_feature4_tab()

    # Feature 1: Sales Analysis
    def build_feature1_tab(self):
        frame = self.tab_feature1

        tk.Label(frame, text="Enter game title for sales analysis:").pack(pady=10)
        self.f1_entry = tk.Entry(frame, width=40)
        self.f1_entry.pack()

        tk.Button(
            frame,
            text="Generate Chart",
            command=self.do_feature1
        ).pack(pady=10)

    def do_feature1(self):
        game_name = self.f1_entry.get().strip()

        if not game_name:
            messagebox.showwarning("Missing Input", "Enter a game title.")
            return

        success = feature1.run_gui_feature1(self.data, game_name)

        if not success:
            messagebox.showerror(
                "Not Found",
                f"No sales data found for '{game_name}'"
            )

    # Feature 2: Search
    def build_feature2_tab(self):
        frame = self.tab_feature2

        tk.Label(frame, text="Enter search keyword:").pack(pady=10)
        self.f2_entry = tk.Entry(frame, width=40)
        self.f2_entry.pack()

        tk.Button(frame, text="Search", command=self.do_search).pack(pady=10)

        self.f2_output = tk.Text(frame, height=22)
        self.f2_output.pack(fill="both", expand=True)

    def do_search(self):
        keyword = self.f2_entry.get().strip()
        results = feature2.search_games(self.data, keyword)

        self.f2_output.delete("1.0", tk.END)

        if not results:
            self.f2_output.insert(tk.END, "No results found.")
            return

        for g in results:
            self.f2_output.insert(
                tk.END,
                f"{g['Title']} | {g['Platform']} | {g['Genre']}\n"
            )

    # Feature 3: Recommendations
    def build_feature3_tab(self):
        frame = self.tab_feature3

        tk.Label(frame, text="Enter a game title:").pack(pady=10)
        self.f3_entry = tk.Entry(frame, width=40)
        self.f3_entry.pack()

        tk.Button(
            frame,
            text="Get Recommendations",
            command=self.do_feature3
        ).pack(pady=10)

        self.f3_output = tk.Text(frame, height=22)
        self.f3_output.pack(fill="both", expand=True)

    def do_feature3(self):
        title = self.f3_entry.get().strip()
        results = feature3.recommend_games(self.data, title)

        self.f3_output.delete("1.0", tk.END)

        if not results:
            self.f3_output.insert(
                tk.END,
                "No recommendations available."
            )
            return

        for g in results:
            self.f3_output.insert(
                tk.END,
                f"{g['Title']} | {g['Platform']} | {g['Genre']}\n"
            )

    # Feature 4: Top 5 Leaderboards
    def build_feature4_tab(self):
        frame = self.tab_feature4

        tk.Label(
            frame,
            text="Top 5 Games by Region",
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Button(
            frame,
            text="Show Leaderboards",
            command=self.do_feature4
        ).pack(pady=10)

        self.f4_output = tk.Text(frame, height=25)
        self.f4_output.pack(fill="both", expand=True)

    def do_feature4(self):
        results = feature4.top_five_games_by_region_gui(self.data)
        self.f4_output.delete("1.0", tk.END)

        for region, games in results.items():
            self.f4_output.insert(
                tk.END,
                f"\n=== {region} ===\n"
            )

            for i, g in enumerate(games, start=1):
                self.f4_output.insert(
                    tk.END,
                    f"{i}. {g['Title']} ({g['Platform']}) — {g['Global_Sales']}m\n"
                )
