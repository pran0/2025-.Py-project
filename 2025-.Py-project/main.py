import features.feature1 as feature1
import features.feature2 as feature2
import features.feature3 as feature3
import features.feature4 as feature4

from config import file_path
from loader import init             # moved from gui.py import
from gui import GameApp


def main():
    print("Loading game data...")

    try:
        database = init(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    print(f"Loaded {len(database)} games.")

    while True:
        print("\n1. Feature 2 (Search)")
        print("2. Feature 3 (Recommendations)")
        print("3. Feature 4 (Top 5 Games by Region)")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            feature2.run(database)

        elif choice == "2":
            feature3.run(database)

        elif choice == "3":
            feature4.run(database)

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    app = GameApp()
    app.mainloop() 
