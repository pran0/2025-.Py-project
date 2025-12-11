# feature1.py — Sales Visualization System

# library set up
import csv                      # the video game sales csv
import matplotlib.pyplot as plt # library used for the bar graph
import sys                      # if an errors were to occur it just helps exit the program

# tells the script what we want the important columns to be called
GAME_COLUMN_HEADER = 'Title'        
PLATFORM_COLUMN_HEADER = 'Platform' .

# defines the 5 sales regions that will eventually be used for the x axis
SALES_COLUMNS_HEADERS = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
REGION_LABELS = ['North America', 'Europe', 'Japan', 'Other', 'Global']

# the datafile location
FILE_PATH = 'games.csv'

# This dictionary assigns a unique color to almost every console platform.
PLATFORM_COLORS = {

    # --- Atari & Other Classics ---
    '2600': 'brown',        # The old school Atari 2600
    
    # --- Nintendo Family ---
    'NES': 'red',           # The original Nintendo
    'SNES': 'darkred',      # The Super Nintendo
    'N64': 'rebeccapurple', # The iconic Nintendo 64
    'GC': 'mediumorchid',   # GameCube
    'Wii': 'skyblue',       # Wii
    'WiiU': 'dodgerblue',   # Wii U
    'DS': 'darkblue',       # Nintendo DS
    '3DS': 'deeppink',      # Nintendo 3DS
    'GB': 'gold',           # Original Game Boy
    'GBA': 'orange',        # Game Boy Advance
    'WS': 'silver',         # WonderSwan
    
    # --- Sony PlayStation Family ---
    'PS': 'teal',           # The first PlayStation (PS1)
    'PS2': 'navy',          # PlayStation 2
    'PS3': 'blue',          # PlayStation 3
    'PS4': 'darkblue',      # PlayStation 4
    'PSV': 'lightcoral',    # PlayStation Vita
    'PSP': 'coral',         # PlayStation Portable

    # --- Microsoft Xbox Family ---
    'XB': 'darkgreen',      # The first Xbox
    'X360': 'forestgreen',  # Xbox 360
    'XOne': 'olivedrab',    # Xbox One
    
    # --- Sega Family ---
    'GEN': 'peru',          # Genesis / Mega Drive
    'GG': 'saddlebrown',    # Game Gear
    'DC': 'darkorange',     # Dreamcast
    'SAT': 'chocolate',     # Saturn
    'SCD': 'tan',           # Sega CD

    # --- Other Platforms ---
    'PC': 'black',          # Personal Computer
    '3DO': 'dimgray',       # 3DO
    'NG': 'olive',          # Neo Geo
    'TG16': 'darkslategray', # TurboGrafx-16
    'PCFX': 'lightslategray',# PC-FX
    
    # --- Default Color ---
    'DEFAULT': 'gray',      # If we don't recognize the platform, we'll just use gray. AI added this in don't think its needed but whatever
}


def load_data(file_path):
    """
    This function reads the game data from the CSV file and cleans it up.
    
    It converts every row into a standardized Python dictionary.
    Crucially, it's forgiving: it works whether the original headers are 'Title' or 'name', 
    'NA_Sales' or 'na_sales', and makes sure all sales numbers are actual decimal values.
    """
    data = [] # This is where we'll keep all the game records once they're processed.
    
    try:
        # open the file and use utf-8 encoding to handle all kinds of characters. utf-8 converts characters to binary so its easier for the program to read
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            # DictReader is great because it gives us dictionaries right away, using the column headers as keys
            reader = csv.DictReader(file)
            
            for row in reader:
                # checks for the title and platform
                name = row.get('name') or row.get('Title')
                platform = row.get('platform') or row.get('Platform')
                
                # if a row missing a name or a platform, we just skip it entirely
                if not name or not platform:
                    continue

                # Ncreates a standardized dictionary structure that the rest of our script expects
                fixed_row = {
                    # Get the title and platform cleaning up whitespace too
                    'Title': (row.get('Title') or row.get('name') or '').strip(),
                    'Platform': (row.get('Platform') or row.get('platform') or '').strip(), 

                    # Convert every sales field to a float. If the field is empty, treat it as 0. done this just incase anything was wrong w the csv data
                    'NA_Sales': float(row.get('NA_Sales') or row.get('na_sales') or 0),
                    'EU_Sales': float(row.get('EU_Sales') or row.get('eu_sales') or 0),
                    'JP_Sales': float(row.get('JP_Sales') or row.get('jp_sales') or 0),
                    'Other_Sales': float(row.get('Other_Sales') or row.get('other_sales') or 0),
                    'Global_Sales': float(row.get('Global_Sales') or row.get('global_sales') or 0),
                }
                
                data.append(fixed_row) # addd the cleaned game data

        print(f"Data loaded successfully from {file_path}. Total rows: {len(data)}")
        return data # hand back the clean list of game data

    except FileNotFoundError:
        # if file isn't where we expected, tell the user and quit
        print(f"Error: CSV file not found at {file_path}.")
        sys.exit(1)
    except Exception as e:
        # any other unexpected loading errors
        print(f"Unexpected error while loading CSV: {e}")
        sys.exit(1)


def filter_game_data(data, game_name):
    """
    This function searches through all our data to find specific entries for one game.
    
    It doesn't require an exact match; searching for "mario" will find "Super Mario Bros."
    The search is also case-insensitive, so capitalization doesn't matter.
    """
    filtered_data = [] # list only contains entries that match the search
    # makes all characters lower case and removes whitespace 
    normalized = game_name.lower().strip()

    for row in data:
        # get the current game title
        title_value = row.get('Title') or row.get('name') or ''
        title = title_value.lower().strip()
        
        # Check if the search term is a part of the games title. this makes the input kinda flexible, obviously we cant account for spelling mistakes
        if normalized in title:
            filtered_data.append(row) # add matching game

    if not filtered_data:
        # if list is empty let the user know nothing was found
        print(f"\nNo sales data found for '{game_name}'.")
        return None

    print(f"Found {len(filtered_data)} entries for '{game_name}'.")
    return filtered_data # return all the entries for that game as in different platforms


def prepare_for_plot(filtered_data):
    """
    This function takes the filtered game data and organizes it for the bar chart.
    
    It groups all the sales figures by platform, making it easy to pass to the plotting function.
    """
    plot_data = {} # a dictionary key = platform, value = a list of its 5 regional sales figures

    for row in filtered_data:
        # gets platform name
        platform = row.get('Platform') or row.get('platform') or 'Unknown'

        sales_values = []
        # loops through the five region columns 
        for logical_col in SALES_COLUMNS_HEADERS:
            upper_key = logical_col       
            lower_key = logical_col.lower() 

            try:
                raw_val = row.get(upper_key)
                if raw_val is None:
                    raw_val = row.get(lower_key)

                # convert the value to a float if missing use 0.0
                value = float(raw_val) if raw_val not in (None, '') else 0.0
                sales_values.append(value)
            
            except (ValueError, TypeError):
                # in case theres a problem converting to a number uses 0.0 to prevent crashing
                sales_values.append(0.0)

        # store the complete set of regional sales for this specific platform version
        plot_data[platform] = sales_values

    return plot_data # data is now usable for the bar chart so it returns the data


def create_bar_chart(plot_data, game_name):
    """
    This is where Matplotlib draws the grouped bar chart.
    
    It shows how a game's sales break down across regions (NA, EU, JP, WW, GL.) 
    for every platform it was released on. 
    """
    
    platforms = list(plot_data.keys())
    num_platforms = len(platforms)
    num_regions = len(SALES_COLUMNS_HEADERS)

    # calculates positions on the x axis for each region group
    x_pos = list(range(num_regions))
    # calculates width of each individual bar, found that 0.8 was the sweetspot as 1 left no gaps between regional sales
    bar_width = 0.8 / num_platforms

    # sets chart window and plotting area
    fig, ax = plt.subplots(figsize=(12, 6))

    # loops through each and every platform found
    for i, platform in enumerate(platforms):
        sales = plot_data[platform]
        
        # grabs colour for the platform
        color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS['DEFAULT'])

        # xalculate the necessary horizontal shift to move the bars into their correct group position
        offset = (i - num_platforms / 2 + 0.5) * bar_width

        # draws bars for the platform
        ax.bar(
            [pos + offset for pos in x_pos], # shifted x positions
            sales,                           # sales figures (bar heights)
            bar_width,                       # calculated width
            label=platform,                  # for the legends
            color=color                      # platform color
        )

    # --- Chart Styling ---
    ax.set_xticks(x_pos)                  # Put the labels under the correct group of bars.
    ax.set_xticklabels(REGION_LABELS)     # Use our friendly region names for the labels.
    ax.set_title(f'Regional Sales Distribution for: {game_name}', fontsize=16)
    ax.set_xlabel('Sales Region', fontsize=12)
    ax.set_ylabel('Sales (in millions)', fontsize=12)
    
    # puts legend in top right corner
    ax.legend(title='Platform', loc='upper right')
    # addslight gray horizontal lines for readability
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # this command makes nothing overlap which is prettty cool
    plt.tight_layout()
    # shows chart
    plt.show()

def run_gui_feature1(full_data, game_name):
    """
    This is the simple function a GUI or a main script 
    would call to run this entire feature.
    
    It handles the three steps: filtering, preparing, and plotting.
    
    Args:
        full_data (list): The list of all cleaned game records.
        game_name (str): The game the user wants to see (e.g., "pokemon").
        
    Returns:
        bool: True if we successfully showed a chart, False if the game wasn't found.
    """
    # finds matching versions of the game
    filtered = filter_game_data(full_data, game_name)
    
    # if finds nothing stops here
    if filtered is None:
        return False

    # 2. structures data for the chart
    plot_data = prepare_for_plot(filtered)
    
    # 3. creates and shows chart
    create_bar_chart(plot_data, game_name)

    return True # finally done hooray
