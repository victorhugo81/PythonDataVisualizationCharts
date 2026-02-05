# piechart.py
"""Pie Chart."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# CONFIGURATION - Change mode here
# ============================================
MODE = 'dark'  # Options: 'dark' or 'light'
# ============================================


def load_data():
    """Load data from CSV file."""
    CSV_FILE = Path("data") / "product_sales.csv"
    
    # Check if file exists
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"{CSV_FILE} not found")
    
    # Load the dataframe
    df = pd.read_csv(CSV_FILE)
    
    # Validate required columns
    if not all(col in df.columns for col in ['Product', 'Sales']):
        raise ValueError("CSV must contain 'Product' and 'Sales' columns")
    
    return df


def main():
    # Load data
    df = load_data()
    
    # Handle edge cases
    if df.empty:
        print("No data to display")
        return
    
    # Check for negative sales values
    if (df['Sales'] < 0).any():
        print("Warning: Negative sales values detected")
        # Optionally filter them out
        df = df[df['Sales'] >= 0]
    
    # Extract labels and values
    labels = df['Product']
    sizes = df['Sales']
    
    # Configure style based on MODE
    if MODE == 'dark':
        plt.style.use('dark_background')
        bg_color = '#1e1e1e'
        text_color = 'white'
        colors = sns.color_palette("bright", n_colors=len(df))
    else:  # light mode
        plt.style.use('default')
        bg_color = 'white'
        text_color = 'black'
        colors = sns.color_palette("pastel", n_colors=len(df))
    
    # Create figure with appropriate background
    fig, ax = plt.subplots(facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        textprops={'color': text_color, 'fontsize': 10}
    )
    
    # Make percentage text bold and slightly larger
    for autotext in autotexts:
        autotext.set_color(text_color)
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    
    # Add title with spacing
    ax.set_title('Sales Distribution by Product', 
                 pad=20, 
                 fontsize=14, 
                 fontweight='bold',
                 color=text_color)
    
    # Make sure the pie chart stays circular
    ax.axis('equal')

    # Make the figure smaller
    fig.set_size_inches(6, 4)
    
    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / f"piechart_{MODE}.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight', facecolor=bg_color)
    print(f"Chart saved to: {OUTPUT_FILE} ({MODE} mode)")
    
    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()