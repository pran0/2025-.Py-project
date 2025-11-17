#Note: Any comment with ** at the end should be taken out before submission and even the line itself is not needed at the end of the code
import pandas as pd

df = pd.read_csv('video_games_sales.csv')

cleaned_df = {
    "Rank": df['rank'],
    "Name": df['name'],
    "Platform": df['platform'],
    "Year": df['year'],
    "Genre": df['genre'],
    "Publisher": df['publisher'],
    "NA_Sales": df['na_sales'],
    "EU_Sales": df['eu_sales'],
    "JP_Sales": df['jp_sales'],
    "Global_Sales": df['global_sales']
}

#The class is subject to change depending on how out code works beacuse the I don't think the init method is correct **
# A class to clean to the data
class CleanData:
    #These are all the columns in the dataset below 
    def __init__(self, rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales):
        self.rank = rank
        self.name = name
        self.platform = platform
        self.genre = genre
        self.publisher = publisher

        #The columns below are all integers/floats
        self.year = year
        self.na_sales = na_sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales

    #This function cleans string values by removing whitespace
    def clean_String(self, value):
        if self.value == str:
            self.value = value
            self.value = df[f"{self.value}"].str.strip()
            return self.value
        else:
            return "Not a String"
        
    #This function converts any strings in the dataset to integers
    def clean_value(self, numeric_value):

        self.numeric_value = numeric_value

        #Whoever can make this function select between int and float please do so because its driving me crazy and I can't be arsed to try it again **
        if isinstance(self.numeric_value, float):
            return self.numeric_value.astype(str).str.strip().astype(float)
        else:
            if isinstance(self.numeric_value, str):
                self.numeric_value = df[f"{self.numeric_value}"].astype(str).str.strip().astype(float)
                return self.numeric_value
            elif isinstance(self.numeric_value, float):
                return self.numeric_value
            else:
                return self.numeric_value.astype(str).str.strip().astype(float)
        
cleanData = CleanData('Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales')
cleaned_Int = cleanData.clean_value(cleaned_df['Year'])
print(cleaned_Int)
