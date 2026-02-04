# hbarchart.py
"""Horizontal Bar Chart."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

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
    
    # Multiple colors for each bar
    pastel_colors = sns.color_palette("pastel", n_colors=len(df))
    
    # Single color update number for different color.
    # pastel_colors = sns.color_palette("pastel")[2]
    
    # Plot - CHANGED TO HORIZONTAL
    plt.figure(figsize=(10, 5))
    plt.barh(  # Changed from plt.bar to plt.barh
        df["Month"],
        df["Sales"],
        color=pastel_colors,
        edgecolor="gray",
        linewidth=0.0,
        height=0.8  # Changed from width to height
    )
    
    # Chart Settings
    plt.title("Monthly Sales Performance", pad=10, fontsize=14, fontweight='bold')
    plt.xlabel("Sales", fontweight='bold')  # Swapped xlabel
    plt.ylabel("Month", fontweight='bold')  # Swapped ylabel
    plt.grid(axis="x", linestyle="-", alpha=0.3)  # Changed from axis="y" to axis="x"
    plt.tight_layout()
    
    # Remove outside border (spines)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
       
    # Make the figure smaller
    plt.gcf().set_size_inches(6, 4)  # Smaller dimensions
    
    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / "hbarchart.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight')  # Lower DPI
    print(f"Chart saved to: {OUTPUT_FILE}")
    
    # Show chart
    plt.show()

if __name__ == "__main__":
    main()