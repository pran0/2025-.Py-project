# feature1.py — Sales Visualization System

import csv
import matplotlib.pyplot as plt
import sys

# defines the columns the script will use 
# NOTE: these are *logical* names; we handle both raw and processed keys in code.
GAME_COLUMN_HEADER = 'Title'        # logical title field
PLATFORM_COLUMN_HEADER = 'Platform' # logical platform field
# logical sales headers (we'll map from either raw or processed)
SALES_COLUMNS_HEADERS = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
REGION_LABELS = ['North America', 'Europe', 'Japan', 'Other', 'Global']

FILE_PATH = 'games.csv'   # updated to relative path for GUI + CLI compatibility

# platform → color mapping (kept exactly as you wrote)
PLATFORM_COLORS = {

    # --- Atari & Other Classics ---
    '2600': 'brown',        # Atari 2600
    
    # --- Nintendo Family ---
    'NES': 'red',           # Nintendo Entertainment System
    'SNES': 'darkred',      # Super Nintendo Entertainment System
    'N64': 'rebeccapurple', # Nintendo 64
    'GC': 'mediumorchid',   # GameCube
    'Wii': 'skyblue',       # Wii
    'WiiU': 'dodgerblue',   # Wii U
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
    """
    Converts CSV rows into a list of dictionaries.
    For CLI use. In the GUI we normally pass in already-processed rows from loader.init().
    
    This version is tolerant: it will work whether the CSV headers use
    lower_snake_case (name, na_sales, ...) or your processed form.
    """
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # require some kind of name + platform
                name = row.get('name') or row.get('Title')
                platform = row.get('platform') or row.get('Platform')
                if not name or not platform:
                    continue

                # normalise into the processed schema used everywhere else
                fixed_row = {
                    'Title': (row.get('Title') or row.get('name') or '').strip(),
                    'Platform': (row.get('Platform') or row.get('platform') or '').strip(),
                    'NA_Sales': float(row.get('NA_Sales') or row.get('na_sales') or 0) ,
                    'EU_Sales': float(row.get('EU_Sales') or row.get('eu_sales') or 0) ,
                    'JP_Sales': float(row.get('JP_Sales') or row.get('jp_sales') or 0) ,
                    'Other_Sales': float(row.get('Other_Sales') or row.get('other_sales') or 0),
                    'Global_Sales': float(row.get('Global_Sales') or row.get('global_sales') or 0),
                }
                data.append(fixed_row)

        print(f"Data loaded successfully from {file_path}. Total rows: {len(data)}")
        return data

    except FileNotFoundError:
        print(f"Error: CSV file not found at {file_path}.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while loading CSV: {e}")
        sys.exit(1)


def filter_game_data(data, game_name):
    """
    Returns list of rows where the game name matches (case-insensitive).
    - Here we allow both exact match AND partial match (quality-of-life).
    - Uses either 'Title' or 'name' depending on what exists.
    """
    filtered_data = []
    normalized = game_name.lower().strip()

    for row in data:
        # be tolerant: look for either 'Title' or 'name'
        title_value = row.get('Title') or row.get('name') or ''
        title = title_value.lower().strip()
        # allow substring match so "mario" will find "Super Mario Bros"
        if normalized in title:
            filtered_data.append(row)

    if not filtered_data:
        print(f"\nNo sales data found for '{game_name}'.")
        return None

    print(f"Found {len(filtered_data)} entries for '{game_name}'.")
    return filtered_data


def prepare_for_plot(filtered_data):
    """
    Convert numeric sales fields into floats.
    Group by platform.
    Tolerant to both raw (na_sales) and processed (NA_Sales) keys.
    """
    plot_data = {}

    for row in filtered_data:
        # platform can be 'Platform' or 'platform'
        platform = row.get('Platform') or row.get('platform') or 'Unknown'

        sales_values = []
        for logical_col in SALES_COLUMNS_HEADERS:
            # map logical 'NA_Sales' to possible keys in the data
            # e.g. 'NA_Sales' or 'na_sales'
            upper_key = logical_col
            lower_key = logical_col.lower()

            try:
                raw_val = row.get(upper_key)
                if raw_val is None:
                    raw_val = row.get(lower_key)

                value = float(raw_val) if raw_val not in (None, '') else 0.0
                sales_values.append(value)
            except (ValueError, TypeError):
                sales_values.append(0.0)

        plot_data[platform] = sales_values

    return plot_data


def create_bar_chart(plot_data, game_name):
    """
    Creates the matplotlib bar chart.
    GUI will display normally using plt.show().
    """

    platforms = list(plot_data.keys())
    num_platforms = len(platforms)
    num_regions = len(SALES_COLUMNS_HEADERS)

    x_pos = list(range(num_regions))
    # bar width 0.8 cause if there is only 1 platform and bar width = 1 it theres no disconnection
    bar_width = 0.8 / num_platforms

    fig, ax = plt.subplots(figsize=(12, 6))

    # iterates through each platform to draw a set of bars through 5 base values (the sales)
    for i, platform in enumerate(platforms):
        sales = plot_data[platform]

        # looks up colour in the dictionary for the specicfic platform graphed
        color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS['DEFAULT'])

        offset = (i - num_platforms / 2 + 0.5) * bar_width

        ax.bar(
            [pos + offset for pos in x_pos],
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

    plt.tight_layout()
    plt.show()  # displays chart


# -----------------------------------------------------
# NEW: GUI-friendly wrapper (minimal modification)
# -----------------------------------------------------
def run_gui_feature1(full_data, game_name):
    """
    GUI wrapper for Feature 1.
    full_data is expected to be a list of dicts (either raw CSV rows OR init() output).
    Returns True if successful, False if game not found.
    """
    filtered = filter_game_data(full_data, game_name)
    if filtered is None:
        return False

    plot_data = prepare_for_plot(filtered)
    create_bar_chart(plot_data, game_name)

    return True
# -----------------------------------------------------
