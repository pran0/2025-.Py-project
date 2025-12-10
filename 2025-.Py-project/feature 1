import csv
import matplotlib.pyplot as plt
import sys

# defines the columns the script will use 
FILE_PATH = 'C:/Users/tluka/OneDrive/Desktop/video_games_sales.csv'
GAME_COLUMN_HEADER = 'name'      # the column header for the game title
PLATFORM_COLUMN_HEADER = 'platform' # the column header for the platform
SALES_COLUMNS_HEADERS = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']
REGION_LABELS = ['North America', 'Europe', 'Japan', 'Other', 'global']

PLATFORM_COLORS = {

    # --- Atari & Other Classics ---
    '2600': 'brown',        # Atari 2600
    
    # --- Nintendo Family ---
    'NES': 'red',           # Nintendo Entertainment System
    'SNES': 'darkred',      # Super Nintendo Entertainment System
    'N64': 'rebeccapurple', # Nintendo 64
    'GC': 'mediumorchid',   # GameCube
    'Wii': 'skyblue',       # Wii
    'WiiU': 'dodgerblue',    # Wii U
    'DS': 'darkblue',       # Nintendo DS
    '3DS': 'deeppink',      # Nintendo 3DS
    'GB': 'gold',           # Game Boy
    'GBA': 'orange',        # Game Boy Advance
    'WS': 'silver',         # WonderSwan
    
    # --- Sony PlayStation Family ---
    'PS': 'teal',           # PlayStation (PS1)
    'PS2': 'navy',          # PlayStation 2
    'PS3': 'blue',          # PlayStation 3
    'PS4': 'darkblue',      # PlayStation 4
    'PSV': 'lightcoral',    # PlayStation Vita
    'PSP': 'coral',         # PlayStation Portable

    # --- Microsoft ---
    'XB': 'darkgreen',      # Xbox (Original)
    'X360': 'forestgreen',  # Xbox 360
    'XOne': 'olivedrab',    # Xbox One
    
    # --- Sega ---
    'GEN': 'peru',          # Genesis / Mega Drive
    'GG': 'saddlebrown',    # Game Gear
    'DC': 'darkorange',     # Dreamcast
    'SAT': 'chocolate',     # Saturn
    'SCD': 'tan',           # Sega CD

    # --- Others ---
    'PC': 'black',          # Personal Computer
    '3DO': 'dimgray',       # 3DO
    'NG': 'olive',          # Neo Geo
    'TG16': 'darkslategray', # TurboGrafx-16
    'PCFX': 'lightslategray',# PC-FX
    
    # --- Default for missing/unknown platforms ---
    'DEFAULT': 'gray',
}


def load_data(file_path):
   # converts csv data into a list of dictionaries
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            # treats each row as a dictionary where keys are the headers
            reader = csv.DictReader(file)
            for row in reader:
                # remove rows with missing data
                if row.get(GAME_COLUMN_HEADER) and row.get(PLATFORM_COLUMN_HEADER):
                    data.append(row)
                    # if anything wrong happens with loading csv file, lowkey threw this in just for an excuse to use except
        print(f"Data loaded successfully from {file_path}. Total rows: {len(data)}")
        return data
    except FileNotFoundError:
        print(f" Error: CSV file not found at {file_path}. Please check the path.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during file loading: {e}")
        sys.exit(1) 

def filter_game_data(data, game_name):
    # scans the list of dictionaries for all rows matching the input game name
    filtered_data = []
    # removes the importance of case sensitivity
    normalized_game_name = game_name.lower().strip()
    
    for row in data:
        # checks row contains the column and if value matches input
        game_title = row.get(GAME_COLUMN_HEADER, '').lower().strip()
        if game_title == normalized_game_name:
            filtered_data.append(row)
            # if no game is found
    if not filtered_data:
        print(f"\nNo sales data found for game: '{game_name}'.")
        print("Please check the spelling or try a different game.")
        return None
    
    print(f"\nFound {len(filtered_data)} platform release(s) for '{game_name}'.")
    return filtered_data

def prepare_for_plot(filtered_data):

    # structures the filtered data for matplotlib converts sales figures to floats and organizes data by platform

    plot_data = {} # key: platform (str), value: List of 5 sales figures (float)
    
    for row in filtered_data:
        platform = row[PLATFORM_COLUMN_HEADER]
        sales_values = []
        
        for col in SALES_COLUMNS_HEADERS:
            try:
                # converts sales string  values to floats (handling potential empty strings or None)
                sales_str = row.get(col, '0.0')
                if sales_str == '': # treats empty string as 0
                     sales_values.append(0.0)
                else:
                    sales_values.append(float(sales_str))
            except ValueError:
                # if conversion fails set to zero
                sales_values.append(0.0) 
        
        plot_data[platform] = sales_values
    
    return plot_data

def create_bar_chart(plot_data, game_name):
    
    
    # lines 129-141 makes the bar chart readable and consistent throughout entries of different games and platforms 

    platforms = list(plot_data.keys())
    num_platforms = len(platforms)
    num_regions = len(SALES_COLUMNS_HEADERS)
    
    x_pos = list(range(num_regions)) 

    # bar width 0.8 cause if there is only 1 platform and bar width = 1 it theres no disconnection between bars in different regions
    bar_width = 0.8 / num_platforms 
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # iterates through each platform to draw a set of bars through 5 base values (the sales)
    for i, platform in enumerate(platforms):
        sales = plot_data[platform]
        
        # looks up colour in the dictionary for the specicfic platform graphed
        color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS['DEFAULT'])
        
        offset = (i - num_platforms / 2 + 0.5) * bar_width
        
        # tells the colour to the ax.bar function
        ax.bar(
            [pos + offset for pos in x_pos],
            # applies colour, bar width, sales and platforms here
            sales,
            bar_width,
            label=platform,
            color=color 
        )
        
    # chart formatting 
    ax.set_xticks(x_pos)
    ax.set_xticklabels(REGION_LABELS)
    ax.set_title(f'Regional Sales Distribution for: {game_name}', fontsize=16)
    ax.set_xlabel('Sales Region', fontsize=12)
    ax.set_ylabel('Sales (in millions)', fontsize=12)
    ax.legend(title='Platform', loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # line 173 prevents overlapping of each individual bar just makes it look a whole lot cleaner and not look like shit

    plt.tight_layout()
    plt.show() # displays chart

# main execution block
if __name__ == "__main__":
    # loads dataset
    full_data = load_data(FILE_PATH)
    
    while True:
        # get user input
        game_name_input = input("\nEnter a video game or 'exit' to quit: ")
        if game_name_input.lower() == 'exit':
            print("Thank you for using the Game Sales Visualizer. ")
            break

        # filters data for requested game
        game_data = filter_game_data(full_data, game_name_input)
        
        if game_data is not None:
            # prepares data for plotting
            plot_data = prepare_for_plot(game_data)
            
            # generates and show the bar chart
            create_bar_chart(plot_data, game_name_input)
