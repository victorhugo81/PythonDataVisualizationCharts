import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

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
    
    # Create figure with smaller size
    fig, ax = plt.subplots(figsize=(7, 4))
    
    # Plot the map (continental US only)
    usa.plot(column='Population', 
             ax=ax, 
             cmap='Blues',
             legend=True,
             edgecolor='black',
             linewidth=0.5,
             missing_kwds={'color': '#eaeaea'})
    
    # Add title with smaller font
    ax.set_title('U.S. States by Population (Continental US)', fontsize=14, pad=15)
    ax.axis('off')
    
    # Ensure output directory exists
    OUTPUT_FILE = Path("output") / "us_population_map.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Save as PNG
    plt.savefig(OUTPUT_FILE, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"Map saved to: {OUTPUT_FILE}")
    
    # Clean up
    plt.close(fig)

if __name__ == "__main__":
    main()