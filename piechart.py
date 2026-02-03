import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from pathlib import Path


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
    
    # Create color gradient (larger values = darker colors)
    norm = Normalize(vmin=min(sizes), vmax=max(sizes))
    colors = cm.Blues(norm(sizes))
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Create pie chart
    plt.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140
    )
    
    # Add title with spacing
    plt.title('Sales Distribution by Product', pad=30, fontsize=16)
    
    # Make sure the pie chart stays circular
    plt.axis('equal')
    
    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / "sales_distribution.png"
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {OUTPUT_FILE}")
    
    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
