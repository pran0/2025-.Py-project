# feature1.py — Sales Visualization System

# --- Library Setup (The Tools We Need) ---
import csv                      # This tool lets us easily read the game data out of a CSV file.
import matplotlib.pyplot as plt # We use this standard library to draw our graphs and charts.
import sys                      # This helps us exit the program cleanly if something goes wrong, like a missing file.

# --- Configuration: Data Column Mappings (Defining What's What) ---

# These constants just tell the script what to call the important columns in our data.
GAME_COLUMN_HEADER = 'Title'        # We'll refer to the game's title using this name.
PLATFORM_COLUMN_HEADER = 'Platform' # This is what we call the column holding the console/platform name.

# This list defines the five regional sales columns we are going to plot.
SALES_COLUMNS_HEADERS = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
# And this list provides the nice, readable names for those regions to display on the chart's X-axis.
REGION_LABELS = ['North America', 'Europe', 'Japan', 'Other', 'Global']

# The location of our game data file.
FILE_PATH = 'games.csv'

# --- Configuration: Platform Color Map (Making the Chart Look Good) ---

# This dictionary assigns a unique color to almost every console platform.
# If a platform isn't listed, it will default to 'gray'.
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
    'DEFAULT': 'gray',      # If we don't recognize the platform, we'll just use gray.
}

# --- Core Functions (The Logic) ---

def load_data(file_path):
    """
    This function reads the game data from the CSV file and cleans it up.
    
    It converts every row into a standardized Python dictionary.
    Crucially, it's forgiving: it works whether the original headers are 'Title' or 'name', 
    'NA_Sales' or 'na_sales', and makes sure all sales numbers are actual decimal values.
    """
    data = [] # This is where we'll keep all the game records once they're processed.
    
    try:
        # We open the file and use utf-8 encoding to handle all kinds of characters.
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            # DictReader is great because it gives us dictionaries right away, using the column headers as keys.
            reader = csv.DictReader(file)
            
            for row in reader:
                # First, check for the title and platform, being flexible about which header they use.
                name = row.get('name') or row.get('Title')
                platform = row.get('platform') or row.get('Platform')
                
                # If a row is missing a name or a platform, we just skip it entirely.
                if not name or not platform:
                    continue

                # Now, create a standardized dictionary structure that the rest of our script expects.
                fixed_row = {
                    # Get the Title and Platform, and clean up any extra spaces around the names.
                    'Title': (row.get('Title') or row.get('name') or '').strip(),
                    'Platform': (row.get('Platform') or row.get('platform') or '').strip(), 

                    # Convert every sales field to a decimal number (float). If the field is empty, treat it as 0.
                    'NA_Sales': float(row.get('NA_Sales') or row.get('na_sales') or 0),
                    'EU_Sales': float(row.get('EU_Sales') or row.get('eu_sales') or 0),
                    'JP_Sales': float(row.get('JP_Sales') or row.get('jp_sales') or 0),
                    'Other_Sales': float(row.get('Other_Sales') or row.get('other_sales') or 0),
                    'Global_Sales': float(row.get('Global_Sales') or row.get('global_sales') or 0),
                }
                
                data.append(fixed_row) # Add the cleaned game record.

        print(f"Data loaded successfully from {file_path}. Total rows: {len(data)}")
        return data # Hand back the complete, clean list of game data.

    except FileNotFoundError:
        # If the file isn't where we expected, tell the user and quit.
        print(f"Error: CSV file not found at {file_path}.")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected loading errors.
        print(f"Unexpected error while loading CSV: {e}")
        sys.exit(1)


def filter_game_data(data, game_name):
    """
    This function searches through all our data to find specific entries for one game.
    
    It doesn't require an exact match; searching for "mario" will find "Super Mario Bros."
    The search is also case-insensitive, so capitalization doesn't matter.
    """
    filtered_data = [] # This list will only contain the entries that match the search.
    # Standardize the search term to lowercase and trim any spaces.
    normalized = game_name.lower().strip()

    for row in data:
        # Get the current game's title, being flexible with the key used.
        title_value = row.get('Title') or row.get('name') or ''
        title = title_value.lower().strip()
        
        # Check if the search term is a part of the game's title.
        if normalized in title:
            filtered_data.append(row) # Add the matching game.

    if not filtered_data:
        # If the list is empty, let the user know we found nothing.
        print(f"\nNo sales data found for '{game_name}'.")
        return None

    print(f"Found {len(filtered_data)} entries for '{game_name}'.")
    return filtered_data # Return all the entries for that game (e.g., all its different platform versions).


def prepare_for_plot(filtered_data):
    """
    This function takes the filtered game data and organizes it for the bar chart.
    
    It groups all the sales figures by platform, making it easy to pass to the plotting function.
    """
    plot_data = {} # Our result: A dictionary where the key is the Platform, and the value is a list of its 5 regional sales figures.

    for row in filtered_data:
        # Get the platform name.
        platform = row.get('Platform') or row.get('platform') or 'Unknown'

        sales_values = []
        # Loop through the five region columns we care about.
        for logical_col in SALES_COLUMNS_HEADERS:
            upper_key = logical_col       
            lower_key = logical_col.lower() 

            try:
                # Try to get the raw sales value from either the standard or lowercase key.
                raw_val = row.get(upper_key)
                if raw_val is None:
                    raw_val = row.get(lower_key)

                # Convert the value to a decimal. If it's missing or blank, use 0.0.
                value = float(raw_val) if raw_val not in (None, '') else 0.0
                sales_values.append(value)
            
            except (ValueError, TypeError):
                # If there's a problem converting to a number, just use 0.0 to prevent crashing.
                sales_values.append(0.0)

        # Store the complete set of regional sales for this specific platform version.
        plot_data[platform] = sales_values

    return plot_data # This data is now perfectly structured for drawing the chart.


def create_bar_chart(plot_data, game_name):
    """
    This is where Matplotlib draws the grouped bar chart.
    
    It shows how a game's sales break down across regions (NA, EU, JP, etc.) 
    for every platform it was released on. 
    """
    
    platforms = list(plot_data.keys())
    num_platforms = len(platforms)
    num_regions = len(SALES_COLUMNS_HEADERS)

    # Calculate the positions on the X-axis for each region group.
    x_pos = list(range(num_regions))
    # Calculate how wide each individual bar should be so they fit next to each other in a group.
    bar_width = 0.8 / num_platforms

    # Set up the chart window and the plotting area.
    fig, ax = plt.subplots(figsize=(12, 6))

    # Loop through each platform we need to plot.
    for i, platform in enumerate(platforms):
        sales = plot_data[platform]
        
        # Grab the right color for the platform (or the default gray).
        color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS['DEFAULT'])

        # Calculate the necessary horizontal shift to move the bars into their correct group position.
        offset = (i - num_platforms / 2 + 0.5) * bar_width

        # Draw the bars for this platform.
        ax.bar(
            [pos + offset for pos in x_pos], # The shifted X-positions
            sales,                           # The sales figures (bar heights)
            bar_width,                       # The width we calculated
            label=platform,                  # Text to show in the legend
            color=color                      # The platform color
        )

    # --- Chart Styling ---
    ax.set_xticks(x_pos)                  # Put the labels under the correct group of bars.
    ax.set_xticklabels(REGION_LABELS)     # Use our friendly region names for the labels.
    ax.set_title(f'Regional Sales Distribution for: {game_name}', fontsize=16)
    ax.set_xlabel('Sales Region', fontsize=12)
    ax.set_ylabel('Sales (in millions)', fontsize=12)
    
    # Place the legend in the top right to explain the colors.
    ax.legend(title='Platform', loc='upper right')
    # Add light gray horizontal lines to help read the sales values.
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Adjust the layout automatically so everything fits nicely.
    plt.tight_layout()
    # Show the chart!
    plt.show()


# -----------------------------------------------------
# Wrapper Function (The main entry point)
# -----------------------------------------------------

def run_gui_feature1(full_data, game_name):
    """
    This is the simple function a Graphical User Interface (GUI) or a main script 
    would call to run this entire feature.
    
    It handles the three steps: filtering, preparing, and plotting.
    
    Args:
        full_data (list): The list of all cleaned game records.
        game_name (str): The game the user wants to see (e.g., "pokemon").
        
    Returns:
        bool: True if we successfully showed a chart, False if the game wasn't found.
    """
    # 1. Find all matching versions of the game.
    filtered = filter_game_data(full_data, game_name)
    
    # If the filter function couldn't find anything, we stop here.
    if filtered is None:
        return False

    # 2. Re-structure the data ready for the chart.
    plot_data = prepare_for_plot(filtered)
    
    # 3. Generate and display the chart.
    create_bar_chart(plot_data, game_name)

    return True # Success!
# -----------------------------------------------------
