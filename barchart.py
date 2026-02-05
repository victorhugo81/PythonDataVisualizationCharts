# barchart.py
"""Bar Chart"""

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
    
    # Load and return the dataframe
    df = pd.read_csv(CSV_FILE)
    return df


def main():
    # Load data
    df = load_data()
    
    # Ensure months are in correct order
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
    df = df.sort_values("Month")
    
    # Configure style based on MODE
    if MODE == 'dark':
        plt.style.use('dark_background')
        bg_color = '#1e1e1e'
        text_color = 'white'
        grid_color = 'gray'
        edge_color = '#555555'
        bar_colors = sns.color_palette("bright", n_colors=len(df))
    else:  # light mode
        plt.style.use('default')
        bg_color = 'white'
        text_color = 'black'
        grid_color = 'gray'
        edge_color = 'gray'
        bar_colors = sns.color_palette("pastel", n_colors=len(df))
    
    # Create figure with appropriate background
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    # Plot
    ax.bar(
        df["Month"],
        df["Sales"],
        color=bar_colors,
        edgecolor=edge_color,
        linewidth=0.0,
        width=0.8
    )
    
    # Chart Settings
    ax.set_title("Monthly Sales Performance", 
                 pad=10, 
                 fontsize=14, 
                 fontweight='bold',
                 color=text_color)
    ax.set_xlabel("Month", fontweight='bold', color=text_color)
    ax.set_ylabel("Sales", fontweight='bold', color=text_color)
    
    # Set tick colors
    ax.tick_params(colors=text_color, which='both')
    
    # Add grid
    ax.grid(axis="y", linestyle="-", alpha=0.3, color=grid_color)
    
    plt.tight_layout()

    # Remove outside border (spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / f"barchart_{MODE}.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight', facecolor=bg_color)
    print(f"Chart saved to: {OUTPUT_FILE} ({MODE} mode)")

    # Show chart
    plt.show()

if __name__ == "__main__":
    main()