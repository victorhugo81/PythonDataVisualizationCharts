import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
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
    
    # Normalize sales for colors
    norm = Normalize(vmin=df["Sales"].min(), vmax=df["Sales"].max())
    colors = cm.Blues(norm(df["Sales"]))
    
    # Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(
        x="Month",
        y="Sales",
        data=df,
        palette=colors,
        edgecolor="gray",
        linewidth=0.6
    )
    
    # Chart Settings
    plt.title("Monthly Sales Performance", fontsize=14)
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / "sales_performance.png"
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {OUTPUT_FILE}")

    # Show chart
    plt.show()

if __name__ == "__main__":
    main()
