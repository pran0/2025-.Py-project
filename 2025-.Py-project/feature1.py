# feature1.py — Sales Visualization System

# This line brings in the csv library so we can read CSV files
import csv
# This line brings in matplotlib so we can create graphs and charts
import matplotlib.pyplot as plt
# This line brings in sys so we can exit the program if there's an error
import sys

# defines the columns the script will use 
# NOTE: these are *logical* names; we handle both raw and processed keys in code.
# This is the name we'll use for the game title column
GAME_COLUMN_HEADER = 'Title'        # logical title field
# This is the name we'll use for the platform column
PLATFORM_COLUMN_HEADER = 'Platform' # logical platform field
# logical sales headers (we'll map from either raw or processed)
# This is a list of all the sales columns we want to display on our chart
SALES_COLUMNS_HEADERS = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
# This is a list of friendly names for each region to show on the chart
REGION_LABELS = ['North America', 'Europe', 'Japan', 'Other', 'Global']

# This is the path to our CSV file with all the game data
FILE_PATH = 'games.csv'   # updated to relative path for GUI + CLI compatibility

# platform → color mapping (kept exactly as you wrote)
# This is a dictionary that tells us what color to use for each gaming platform
PLATFORM_COLORS = {

    # --- Atari & Other Classics ---
    # This sets the color for Atari 2600
    '2600': 'brown',        # Atari 2600
    
    # --- Nintendo Family ---
    # This sets the color for Nintendo Entertainment System
    'NES': 'red',           # Nintendo Entertainment System
    # This sets the color for Super Nintendo Entertainment System
    'SNES': 'darkred',      # Super Nintendo Entertainment System
    # This sets the color for Nintendo 64
    'N64': 'rebeccapurple', # Nintendo 64
    # This sets the color for GameCube
    'GC': 'mediumorchid',   # GameCube
    # This sets the color for Wii
    'Wii': 'skyblue',       # Wii
    # This sets the color for Wii U
    'WiiU': 'dodgerblue',   # Wii U
    # This sets the color for Nintendo DS
    'DS': 'darkblue',       # Nintendo DS
    # This sets the color for Nintendo 3DS
    '3DS': 'deeppink',      # Nintendo 3DS
    # This sets the color for Game Boy
    'GB': 'gold',           # Game Boy
    # This sets the color for Game Boy Advance
    'GBA': 'orange',        # Game Boy Advance
    # This sets the color for WonderSwan
    'WS': 'silver',         # WonderSwan
    
    # --- Sony PlayStation Family ---
    # This sets the color for PlayStation (PS1)
    'PS': 'teal',           # PlayStation (PS1)
    # This sets the color for PlayStation 2
    'PS2': 'navy',          # PlayStation 2
    # This sets the color for PlayStation 3
    'PS3': 'blue',          # PlayStation 3
    # This sets the color for PlayStation 4
    'PS4': 'darkblue',      # PlayStation 4
    # This sets the color for PlayStation Vita
    'PSV': 'lightcoral',    # PlayStation Vita
    # This sets the color for PlayStation Portable
    'PSP': 'coral',         # PlayStation Portable

    # --- Microsoft ---
    # This sets the color for Xbox (Original)
    'XB': 'darkgreen',      # Xbox (Original)
    # This sets the color for Xbox 360
    'X360': 'forestgreen',  # Xbox 360
    # This sets the color for Xbox One
    'XOne': 'olivedrab',    # Xbox One
    
    # --- Sega ---
    # This sets the color for Genesis / Mega Drive
    'GEN': 'peru',          # Genesis / Mega Drive
    # This sets the color for Game Gear
    'GG': 'saddlebrown',    # Game Gear
    # This sets the color for Dreamcast
    'DC': 'darkorange',     # Dreamcast
    # This sets the color for Saturn
    'SAT': 'chocolate',     # Saturn
    # This sets the color for Sega CD
    'SCD': 'tan',           # Sega CD

    # --- Others ---
    # This sets the color for Personal Computer
    'PC': 'black',          # Personal Computer
    # This sets the color for 3DO
    '3DO': 'dimgray',       # 3DO
    # This sets the color for Neo Geo
    'NG': 'olive',          # Neo Geo
    # This sets the color for TurboGrafx-16
    'TG16': 'darkslategray', # TurboGrafx-16
    # This sets the color for PC-FX
    'PCFX': 'lightslategray',# PC-FX
    
    # --- Default for missing/unknown platforms ---
    # This is the color we'll use if we don't recognize the platform
    'DEFAULT': 'gray',
}


# This creates a function that reads the CSV file and loads all the game data
def load_data(file_path):
    """
    Converts CSV rows into a list of dictionaries.
    For CLI use. In the GUI we normally pass in already-processed rows from loader.init().
    
    This version is tolerant: it will work whether the CSV headers use
    lower_snake_case (name, na_sales, ...) or your processed form.
    """
    # This creates an empty list where we'll store all the game data
    data = []
    # This starts a try block to catch any errors that might happen
    try:
        # This opens the CSV file for reading with utf-8 encoding to handle special characters
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            # This creates a reader that automatically reads each row as a dictionary
            reader = csv.DictReader(file)
            # This loops through each row in the CSV file
            for row in reader:
                # require some kind of name + platform
                # This gets the game name from either 'name' or 'Title' column
                name = row.get('name') or row.get('Title')
                # This gets the platform from either 'platform' or 'Platform' column
                platform = row.get('platform') or row.get('Platform')
                # This checks if we're missing the name or platform
                if not name or not platform:
                    # This skips this row and moves to the next one
                    continue

                # normalise into the processed schema used everywhere else
                # This creates a standardized dictionary with all the game information
                fixed_row = {
                    # This gets the title and removes extra spaces
                    'Title': (row.get('Title') or row.get('name') or '').strip(),
                    # This gets the platform and removes extra spaces
                    'Platform': (row.get('Platform') or row.get('platform') or '').strip(),
                    # This gets North America sales and converts to a decimal number (or 0 if missing)
                    'NA_Sales': float(row.get('NA_Sales') or row.get('na_sales') or 0) ,
                    # This gets Europe sales and converts to a decimal number (or 0 if missing)
                    'EU_Sales': float(row.get('EU_Sales') or row.get('eu_sales') or 0) ,
                    # This gets Japan sales and converts to a decimal number (or 0 if missing)
                    'JP_Sales': float(row.get('JP_Sales') or row.get('jp_sales') or 0) ,
                    # This gets Other regions sales and converts to a decimal number (or 0 if missing)
                    'Other_Sales': float(row.get('Other_Sales') or row.get('other_sales') or 0),
                    # This gets Global sales and converts to a decimal number (or 0 if missing)
                    'Global_Sales': float(row.get('Global_Sales') or row.get('global_sales') or 0),
                }
                # This adds this game to our data list
                data.append(fixed_row)

        # This prints a success message showing how many games were loaded
        print(f"Data loaded successfully from {file_path}. Total rows: {len(data)}")
        # This returns the complete list of game data
        return data

    # This catches the error if the file doesn't exist
    except FileNotFoundError:
        # This prints an error message
        print(f"Error: CSV file not found at {file_path}.")
        # This exits the program with an error code
        sys.exit(1)
    # This catches any other unexpected errors
    except Exception as e:
        # This prints what the error was
        print(f"Unexpected error while loading CSV: {e}")
        # This exits the program with an error code
        sys.exit(1)


# This creates a function that finds all games matching a specific name
def filter_game_data(data, game_name):
    """
    Returns list of rows where the game name matches (case-insensitive).
    - Here we allow both exact match AND partial match (quality-of-life).
    - Uses either 'Title' or 'name' depending on what exists.
    """
    # This creates an empty list where we'll store matching games
    filtered_data = []
    # This converts the search name to lowercase and removes extra spaces
    normalized = game_name.lower().strip()

    # This loops through each game in our data
    for row in data:
        # be tolerant: look for either 'Title' or 'name'
        # This gets the game's title from either column name
        title_value = row.get('Title') or row.get('name') or ''
        # This converts the title to lowercase and removes extra spaces
        title = title_value.lower().strip()
        # allow substring match so "mario" will find "Super Mario Bros"
        # This checks if our search term appears anywhere in the game's title
        if normalized in title:
            # This adds this matching game to our filtered list
            filtered_data.append(row)

    # This checks if we didn't find any matching games
    if not filtered_data:
        # This prints a message saying no data was found
        print(f"\nNo sales data found for '{game_name}'.")
        # This returns None to indicate no matches
        return None

    # This prints how many matching games we found
    print(f"Found {len(filtered_data)} entries for '{game_name}'.")
    # This returns the list of matching games
    return filtered_data


# This creates a function that prepares the data to be graphed
def prepare_for_plot(filtered_data):
    """
    Convert numeric sales fields into floats.
    Group by platform.
    Tolerant to both raw (na_sales) and processed (NA_Sales) keys.
    """
    # This creates an empty dictionary where we'll organize sales data by platform
    plot_data = {}

    # This loops through each game we want to plot
    for row in filtered_data:
        # platform can be 'Platform' or 'platform'
        # This gets the platform name, defaulting to 'Unknown' if missing
        platform = row.get('Platform') or row.get('platform') or 'Unknown'

        # This creates an empty list for this game's sales in each region
        sales_values = []
        # This loops through each sales column (NA, EU, JP, Other, Global)
        for logical_col in SALES_COLUMNS_HEADERS:
            # map logical 'NA_Sales' to possible keys in the data
            # e.g. 'NA_Sales' or 'na_sales'
            # This stores the uppercase version of the column name
            upper_key = logical_col
            # This stores the lowercase version of the column name
            lower_key = logical_col.lower()

            # This starts a try block to catch errors converting to numbers
            try:
                # This tries to get the sales value using the uppercase key first
                raw_val = row.get(upper_key)
                # This checks if that didn't work
                if raw_val is None:
                    # This tries the lowercase key instead
                    raw_val = row.get(lower_key)

                # This converts the value to a decimal number, or uses 0.0 if it's empty
                value = float(raw_val) if raw_val not in (None, '') else 0.0
                # This adds this sales value to our list
                sales_values.append(value)
            # This catches errors when converting to a number fails
            except (ValueError, TypeError):
                # This adds 0.0 as a safe default
                sales_values.append(0.0)

        # This stores the sales values for this platform in our dictionary
        plot_data[platform] = sales_values

    # This returns the organized data ready for graphing
    return plot_data


# This creates a function that draws the bar chart
def create_bar_chart(plot_data, game_name):
    """
    Creates the matplotlib bar chart.
    GUI will display normally using plt.show().
    """

    # This gets a list of all the platforms we're graphing
    platforms = list(plot_data.keys())
    # This counts how many platforms we have
    num_platforms = len(platforms)
    # This counts how many regions we're showing (should be 5)
    num_regions = len(SALES_COLUMNS_HEADERS)

    # This creates a list of x-axis positions for our bars (0, 1, 2, 3, 4)
    x_pos = list(range(num_regions))
    # bar width 0.8 cause if there is only 1 platform and bar width = 1 it theres no disconnection
    # This calculates how wide each bar should be based on how many platforms we have
    bar_width = 0.8 / num_platforms

    # This creates a new figure and axis for our chart that's 12 inches wide and 6 inches tall
    fig, ax = plt.subplots(figsize=(12, 6))

    # iterates through each platform to draw a set of bars through 5 base values (the sales)
    # This loops through each platform and its index number
    for i, platform in enumerate(platforms):
        # This gets the sales values for this platform
        sales = plot_data[platform]

        # looks up colour in the dictionary for the specicfic platform graphed
        # This looks up what color to use for this platform, or uses gray if not found
        color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS['DEFAULT'])

        # This calculates how much to shift this platform's bars to the left or right
        offset = (i - num_platforms / 2 + 0.5) * bar_width

        # This draws the bars for this platform
        ax.bar(
            # This shifts each bar position by the offset
            [pos + offset for pos in x_pos],
            # This provides the height of each bar (the sales values)
            sales,
            # This sets the width of each bar
            bar_width,
            # This sets the label for the legend
            label=platform,
            # This sets the color of the bars
            color=color
        )

    # chart formatting 
    # This sets where the labels should appear on the x-axis
    ax.set_xticks(x_pos)
    # This sets what text to show at each x-axis position
    ax.set_xticklabels(REGION_LABELS)
    # This sets the title at the top of the chart
    ax.set_title(f'Regional Sales Distribution for: {game_name}', fontsize=16)
    # This sets the label for the x-axis (horizontal)
    ax.set_xlabel('Sales Region', fontsize=12)
    # This sets the label for the y-axis (vertical)
    ax.set_ylabel('Sales (in millions)', fontsize=12)
    # This creates a legend box in the upper right showing what each color means
    ax.legend(title='Platform', loc='upper right')
    # This adds horizontal grid lines to make the chart easier to read
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # This adjusts the spacing so nothing gets cut off
    plt.tight_layout()
    # displays chart
    # This actually shows the chart window to the user
    plt.show()


# -----------------------------------------------------
# NEW: GUI-friendly wrapper (minimal modification)
# -----------------------------------------------------
# This creates a wrapper function that the GUI can easily call
def run_gui_feature1(full_data, game_name):
    """
    GUI wrapper for Feature 1.
    full_data is expected to be a list of dicts (either raw CSV rows OR init() output).
    Returns True if successful, False if game not found.
    """
    # This filters the data to find games matching the name
    filtered = filter_game_data(full_data, game_name)
    # This checks if no games were found
    if filtered is None:
        # This returns False to indicate failure
        return False

    # This prepares the filtered data for plotting
    plot_data = prepare_for_plot(filtered)
    # This creates and displays the bar chart
    create_bar_chart(plot_data, game_name)

    # This returns True to indicate success
    return True
# -----------------------------------------------------
