# piechart.py
"""Donut Chart."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


def load_data():
    """Load data from CSV file."""
    CSV_FILE = Path("data") / "product_sales.csv"

    if not CSV_FILE.exists():
        raise FileNotFoundError(f"{CSV_FILE} not found")

    df = pd.read_csv(CSV_FILE)

    if not all(col in df.columns for col in ['Product', 'Sales']):
        raise ValueError("CSV must contain 'Product' and 'Sales' columns")

    return df


def main():
    df = load_data()

    if df.empty:
        print("No data to display")
        return

    if (df['Sales'] < 0).any():
        print("Warning: Negative sales values detected")
        df = df[df['Sales'] >= 0]

    labels = df['Product']
    sizes = df['Sales']

    pastel_colors = sns.color_palette("pastel", n_colors=len(df))

    # Create DONUT chart
    plt.pie(
        sizes,
        labels=labels,
        colors=pastel_colors,
        autopct='%1.1f%%',
        startangle=140,
        wedgeprops={"width": 0.45},
        pctdistance=0.75,     # move % outside
        labeldistance=1.10    # move product labels further out
    )

    plt.title(
        'Sales Distribution by Product',
        pad=10,
        fontsize=14,
        fontweight='bold'
    )

    plt.axis('equal')

    plt.gcf().set_size_inches(6, 4)

    OUTPUT_FILE = Path("output") / "donutchart.png"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(OUTPUT_FILE, dpi=72, bbox_inches='tight')
    print(f"Chart saved to: {OUTPUT_FILE}")

    plt.show()


if __name__ == "__main__":
    main()
