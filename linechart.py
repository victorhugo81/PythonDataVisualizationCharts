# linechart.py
"""Line Chart."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# CONFIGURATION - Change mode here
# ============================================
MODE = 'light'  # Options: 'dark' or 'light'
# ============================================


def load_data():
    """Load data from CSV file."""
    CSV_FILE = Path("data") / "monthly_sales.csv"
    
    # Check if file exists
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"{CSV_FILE} not found")
    
    # Load the dataframe
    df = pd.read_csv(CSV_FILE)
    
    # Validate required columns
    required_cols = ['Month', 'Sales']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"CSV must contain columns: {required_cols}")
    
    return df


def main():
    # Load data
    df = load_data()
    
    # Configure style based on MODE
    if MODE == 'dark':
        plt.style.use('dark_background')
        bg_color = '#1e1e1e'
        text_color = 'white'
        grid_color = 'gray'
        marker_color = sns.color_palette("bright")[1]
        line_color = sns.color_palette("bright")[2]
    else:  # light mode
        plt.style.use('default')
        bg_color = 'white'
        text_color = 'black'
        grid_color = 'gray'
        marker_color = sns.color_palette("pastel")[1]
        line_color = sns.color_palette("pastel")[2]
    
    # Create figure with appropriate background
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    # Create line chart
    ax.plot(
        df['Month'],
        df['Sales'],
        marker='o',
        markerfacecolor=marker_color,
        linestyle='-',
        color=line_color,
        linewidth=2
    )

    # Add title and axis labels
    ax.set_title('Monthly Sales Trend', 
                 pad=10, 
                 fontsize=14, 
                 fontweight='bold',
                 color=text_color)
    ax.set_xlabel('Month', fontweight='bold', color=text_color)
    ax.set_ylabel('Sales', fontweight='bold', color=text_color)
    
    # Set tick colors
    ax.tick_params(colors=text_color, which='both')
    
    # Add grid
    ax.grid(True, linestyle='-', alpha=0.3, color=grid_color)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Remove outside border (spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / f"linechart_{MODE}.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight', facecolor=bg_color)
    print(f"Chart saved to: {OUTPUT_FILE} ({MODE} mode)")

    # Show chart
    plt.show()


if __name__ == "__main__":
    main()