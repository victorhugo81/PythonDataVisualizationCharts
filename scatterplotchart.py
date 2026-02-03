import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

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
    
    # Validate Sales column is numeric
    if not pd.api.types.is_numeric_dtype(df['Sales']):
        raise ValueError("Sales column must contain numeric values")
    
    return df


def main():
    # Load data
    df = load_data()
    
    # Handle edge cases
    if df.empty:
        print("No data to display")
        return
    
    # Create figure and axis explicitly
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Create scatter plot
    ax.scatter(df['Month'], df['Sales'], color='blue', alpha=0.7)
    
    # Add title and axis labels
    ax.set_title('Sales Scatter Plot', pad=20)
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    
    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Rotate x-axis labels if they're text to prevent overlap
    plt.xticks(rotation=45, ha='right')
    
    # Ensure output directory exists
    OUTPUT_FILE = Path("output") / "scatterplotchart.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the figure
    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight')
    print(f"Chart saved to: {OUTPUT_FILE}")
    
    # Show the plot
    plt.show()
    
    # Clean up
    plt.close(fig)

if __name__ == "__main__":
    main()