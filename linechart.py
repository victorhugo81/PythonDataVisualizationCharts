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
    
    return df


def main():
    # Load data
    df = load_data()
    
    # Create line chart
    plt.plot(
        df['Month'],
        df['Sales'],
        marker='o',
        linestyle='--',
        color='blue',
        linewidth=2
    )

    # Add title and axis labels
    plt.title('Monthly Sales Trend', fontsize=16, pad=20)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sales', fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Make the figure smaller
    plt.gcf().set_size_inches(6, 4)  # Smaller dimensions

    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / "linechart.png"
    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight')
    print(f"Chart saved to: {OUTPUT_FILE}")

    # Show chart
    plt.show()


if __name__ == "__main__":
    main()