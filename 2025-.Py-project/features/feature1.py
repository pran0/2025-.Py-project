# feature1.py — Sales Visualization System

# Imports
import csv
import matplotlib.pyplot as plt
import sys

# Column names
GAME_COLUMN_HEADER = 'Title'
PLATFORM_COLUMN_HEADER = 'Platform'

# Sales regions
SALES_COLUMNS_HEADERS = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
REGION_LABELS = ['North America', 'Europe', 'Japan', 'Other', 'Global']

# Data file path
FILE_PATH = 'games.csv'

# Platform color mapping
PLATFORM_COLORS = {
    '2600': 'brown',

    'NES': 'red',
    'SNES': 'darkred',
    'N64': 'rebeccapurple',
    'GC': 'mediumorchid',
    'Wii': 'skyblue',
    'WiiU': 'dodgerblue',
    'DS': 'darkblue',
    '3DS': 'deeppink',
    'GB': 'gold',
    'GBA': 'orange',
    'WS': 'silver',

    'PS': 'teal',
    'PS2': 'navy',
    'PS3': 'blue',
    'PS4': 'darkblue',
    'PSV': 'lightcoral',
    'PSP': 'coral',

    'XB': 'darkgreen',
    'X360': 'forestgreen',
    'XOne': 'olivedrab',

    'GEN': 'peru',
    'GG': 'saddlebrown',
    'DC': 'darkorange',
    'SAT': 'chocolate',
    'SCD': 'tan',

    'PC': 'black',
    '3DO': 'dimgray',
    'NG': 'olive',
    'TG16': 'darkslategray',
    'PCFX': 'lightslategray',

    'DEFAULT': 'gray',
}


# Load and clean CSV data
def load_data(file_path):
    data = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row.get('name') or row.get('Title')
                platform = row.get('platform') or row.get('Platform')

                if not name or not platform:
                    continue

                fixed_row = {
                    'Title': (row.get('Title') or row.get('name') or '').strip(),
                    'Platform': (row.get('Platform') or row.get('platform') or '').strip(),
                    'NA_Sales': float(row.get('NA_Sales') or row.get('na_sales') or 0),
                    'EU_Sales': float(row.get('EU_Sales') or row.get('eu_sales') or 0),
                    'JP_Sales': float(row.get('JP_Sales') or row.get('jp_sales') or 0),
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


# Filter games by title
def filter_game_data(data, game_name):
    filtered_data = []
    normalized = game_name.lower().strip()

    for row in data:
        title_value = row.get('Title') or row.get('name') or ''
        title = title_value.lower().strip()

        if normalized in title:
            filtered_data.append(row)

    if not filtered_data:
        print(f"\nNo sales data found for '{game_name}'.")
        return None

    print(f"Found {len(filtered_data)} entries for '{game_name}'.")
    return filtered_data


# Prepare data for plotting
def prepare_for_plot(filtered_data):
    plot_data = {}

    for row in filtered_data:
        platform = row.get('Platform') or row.get('platform') or 'Unknown'
        sales_values = []

        for logical_col in SALES_COLUMNS_HEADERS:
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


# Create grouped bar chart
def create_bar_chart(plot_data, game_name):
    platforms = list(plot_data.keys())
    num_platforms = len(platforms)
    num_regions = len(SALES_COLUMNS_HEADERS)

    x_pos = list(range(num_regions))
    bar_width = 0.8 / num_platforms

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, platform in enumerate(platforms):
        sales = plot_data[platform]
        color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS['DEFAULT'])
        offset = (i - num_platforms / 2 + 0.5) * bar_width

        ax.bar(
            [pos + offset for pos in x_pos],
            sales,
            bar_width,
            label=platform,
            color=color
        )

    ax.set_xticks(x_pos)
    ax.set_xticklabels(REGION_LABELS)
    ax.set_title(f'Regional Sales Distribution for: {game_name}', fontsize=16)
    ax.set_xlabel('Sales Region', fontsize=12)
    ax.set_ylabel('Sales (in millions)', fontsize=12)
    ax.legend(title='Platform', loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


# GUI entry point
def run_gui_feature1(full_data, game_name):
    filtered = filter_game_data(full_data, game_name)

    if filtered is None:
        return False

    plot_data = prepare_for_plot(filtered)
    create_bar_chart(plot_data, game_name)

    return True
