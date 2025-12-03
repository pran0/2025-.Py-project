#Note: Under construction when I am done I will update it again and i added that recommend feature cause i liked the idea 
#But I don't really like the leaderboard thing because their aren't any players in this it's just game sales(my opinion)
from pathlib import Path
import csv

path = Path('video_games_sales.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

Rank, Name, Platform, Year, Genre, Publisher, Na_sales, Eu_sales, Jp_sales, Other_sales, Global_sales = [], [], [], [], [], [], [], [], [], [], []

for row in reader:
    rank = str(row[0])
    name = str(row[1])
    platform = str(row[2])
    year = str(row[3])
    genre = str(row[4])
    publisher = str(row[5])
    na_sales = str(row[6])
    eu_sales = str(row[7])
    jp_sales = str(row[8])
    other_sales = str(row[9])
    global_sales = str(row[10])
    Rank.append(rank)
    Name.append(name)
    Platform.append(platform)
    Year.append(year)
    Genre.append(genre)
    Publisher.append(publisher)
    Na_sales.append(na_sales)
    Eu_sales.append(eu_sales)
    Jp_sales.append(jp_sales)
    Other_sales.append(other_sales)
    Global_sales.append(global_sales)

Rank_values = [int(x) for x in Rank]
Name_values = [str(x) for x in Name]
Platform_values = [str(x) for x in Platform]
Year_values = [float(x) for x in Year]
Genre_values = [str(x) for x in Genre]
Publisher_values = [str(x) for x in Publisher]
Na_sales_values = [float(x) for x in Na_sales]
Eu_sales_values = [float(x) for x in Eu_sales]
Jp_sales_values = [float(x) for x in Jp_sales]
Other_sales_values = [float(x) for x in Other_sales]
Global_sales_values = [float(x) for x in Global_sales]

def recommend():
    question = input("Do you want to enter a game name(Y)? or Do you want to some to be recommended to you(N)?:")
    if question == "Y":
        selected_name = input("Enter the name of the game: ")
        #This converts the elements of Name into a string
        selected_name = Name_values
        if selected_name in Name:
            print(f"{selected_name} The list below are top five most sold games "/
                  f"{Name[0:4]}" )
        else:
            print("The name you entered is not a part of the games available")
            ans = input("Would you like to see a few of the games listed (Y/N):")
            if ans == "Y":
                print(Name[0:50])
            elif ans == "N":
                print("Okay that's fine")
            else:
                print("")

    elif question == "N":
        #This selectes all apperances of the action genre in the dataset and converts it to an array that has the index
        genre_type = "Action"
        indices_g = [i for i, x in enumerate(Genre) if x == genre_type]

        #This converts all the values into a float
        indices_gs = Global_sales_values

        #This for loop indexes all the elements of the "Global Sales" array
        index_gs = []
        for index, value in enumerate(indices_gs):
            index_gs.append(index)
        print(index_gs)

        #To get the common values in a set
        common = set(indices_g) & set(index_gs)
        print(common)

recommend()
