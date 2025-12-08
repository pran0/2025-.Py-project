# main function
from pathlib import Path

import csv

#import feature1
import feature2 
import feature3
#import feature4

#------------------------
# load csv so it can be read
#------------------------

file_path = 'games.csv'  #path to the csv file

def init(file_path): #defining a function to load the data from the csv file
    games= [] #creating an empty dictionary to store the data

    with open(file_path, 'r', encoding="utf-8") as file: #read the csv file not write, then pass in the file so that it can be read
        reader = csv.DictReader(file) #DictReader reads each row and creats a dictionary


    #now iterate through each row of games.csv
        for row in reader:
            try:
                game = { #each row must be validated so all values are of same data type, as well as some input validation
                    'Title': row['name'],  # name → Title
                    'Platform': row['platform'],  
                    'Year_of_Release': int(row['year']) if row['year'] else None,
                    'Genre': row['genre'],
                    'Publisher': row['publisher'],
                    'NA_Sales': float(row['na_sales']) if row['na_sales'] else 0.0,
                    'EU_Sales': float(row['eu_sales']) if row['eu_sales'] else 0.0,
                    'JP_Sales': float(row['jp_sales']) if row['jp_sales'] else 0.0,
                    'Other_Sales': float(row['other_sales']) if row['other_sales'] else 0.0,
                    'Global_Sales': float(row['global_sales']) if row['global_sales'] else 0.0,
                }
        
                games.append(game) #append each game to the games list
            except ValueError:

                continue 
    return games #return the list of games

#------------------------
# function: display_main_menu
# shows the main menu options
# choices for user to select from
#------------------------

def display_main_menu():
    print("WELCOME TO THE GAME DATABASE!")
    print("1. Feature 1: Summary / Analysis")
    print("2. Feature 2: Search & Filtering")
    print("3. Feature 3: Game recommendations")
    print("4. Feature 4: Leaderboards")
    print("5. Exit")


#------------------------
# function: main
# first instance of the program running
#------------------------

def main():
    print("Loading game data...")

    # read the csv file
    try:
        database = init(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    
    print(f"loaded {len(database)} games successfully.")

    #loop for user input, display main menu called
    # it only stops when the user chooses to quit
    while True:
        display_main_menu()
        choice = input("Please choose an option: ").strip().upper()

        #if choice =="1":
            #feature1.run(database)

        if choice == "2":
            feature2.run(database)

        elif choice == "3":
            feature3.run(database)

        #elif choice == "4":
            #feature4.run(database)

        elif choice == "5":
            print("Goodbye! Thanks for using the Game Database!")
            break

        else:
            print("Oops! That's not a valid choice. Try again!")


if __name__ == "__main__":
    main()




