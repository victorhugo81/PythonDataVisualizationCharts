import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# CONFIGURATION - Change mode here
# ============================================
MODE = 'light'  # Options: 'dark' or 'light'
# ============================================


def load_data():
    """Load data from CSV file."""
    CSV_FILE = Path("data") / "states.csv"
    
    # Check if file exists
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"{CSV_FILE} not found")
    
    # Load the dataframe
    df = pd.read_csv(CSV_FILE)
    
    # Validate required columns
    required_cols = ['State', 'Code', 'Population']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"CSV must contain columns: {required_cols}")
    
    return df

def main():
    # Load data
    df = load_data()
    
    # Handle edge cases
    if df.empty:
        print("No data to display")
        return
    
    # Load US states shapefile
    url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_1_states_provinces.zip"
    states = gpd.read_file(url)
    
    # Filter for USA (excluding Alaska and Hawaii for better visualization)
    usa = states[states['admin'] == 'United States of America']
    usa = usa[~usa['postal'].isin(['AK', 'HI'])]  # Exclude Alaska and Hawaii
    
    # Merge with population data
    usa = usa.merge(df, left_on='postal', right_on='Code', how='left')
    
    # Configure style based on MODE
    if MODE == 'dark':
        plt.style.use('dark_background')
        bg_color = '#1e1e1e'
        text_color = 'white'
        edge_color = '#555555'
        missing_color = '#2a2a2a'
        cmap = 'Blues'  # Blues works well on dark backgrounds
    else:  # light mode
        plt.style.use('default')
        bg_color = 'white'
        text_color = 'black'
        edge_color = 'black'
        missing_color = '#eaeaea'
        cmap = 'Blues'
    
    # Create figure with smaller size and appropriate background
    fig, ax = plt.subplots(figsize=(7, 4), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    # Plot the map (continental US only)
    usa.plot(column='Population', 
             ax=ax, 
             cmap=cmap,
             legend=True,
             edgecolor=edge_color,
             linewidth=0.5,
             missing_kwds={'color': missing_color})
    
    # Add title with smaller font
    ax.set_title('U.S. States by Population (Continental US)', 
                 fontsize=14, 
                 pad=15,
                 color=text_color)
    ax.axis('off')
    
    # Style the colorbar for dark mode
    if MODE == 'dark':
        # Get the colorbar and style it
        cbar = fig.axes[-1]  # The colorbar is the last axis
        cbar.tick_params(colors=text_color)
        # Style colorbar labels
        plt.setp(plt.getp(cbar, 'yticklabels'), color=text_color)
    
    # Ensure output directory exists
    OUTPUT_FILE = Path("output") / f"us_population_map_{MODE}.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Save as PNG
    plt.savefig(OUTPUT_FILE, dpi=150, bbox_inches='tight', facecolor=bg_color)
    print(f"Map saved to: {OUTPUT_FILE} ({MODE} mode)")
    
    # Clean up
    plt.close(fig)

if __name__ == "__main__":
    main()