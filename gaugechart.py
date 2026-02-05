# gaugechart.py
"""Gauge Chart."""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
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


def create_gauge_chart(value, max_value, title="Performance", mode='light'):
    """Create a gauge chart using matplotlib."""
    
    # Calculate percentage
    percentage = (value / max_value) * 100
    
    # Configure colors based on mode
    if mode == 'dark':
        bg_color = '#1e1e1e'
        text_color = 'white'
        gauge_bg_color = '#3a3a3a'
        gauge_value_color = '#42a5f5'  # Brighter blue for dark mode
        scale_text_color = '#cccccc'
    else:  # light mode
        bg_color = 'white'
        text_color = 'black'
        gauge_bg_color = '#dcdbdb'
        gauge_value_color = '#84d9e0'
        scale_text_color = '#333333'
    
    # Create figure and axis with smaller size
    fig, ax = plt.subplots(figsize=(4, 3), facecolor=bg_color)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-0.2, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor(bg_color)
    
    # Define gauge parameters
    center = (0, 0)
    outer_radius = 1.0
    inner_radius = 0.7
    start_angle = 180
    end_angle = 0
    
    # Create background arc (gray)
    theta_bg = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    x_outer_bg = outer_radius * np.cos(theta_bg)
    y_outer_bg = outer_radius * np.sin(theta_bg)
    x_inner_bg = inner_radius * np.cos(theta_bg)
    y_inner_bg = inner_radius * np.sin(theta_bg)
    
    # Draw gray background
    vertices_bg = list(zip(x_outer_bg, y_outer_bg)) + list(zip(x_inner_bg[::-1], y_inner_bg[::-1]))
    polygon_bg = patches.Polygon(vertices_bg, facecolor=gauge_bg_color, edgecolor='none')
    ax.add_patch(polygon_bg)
    
    # Create value arc (blue)
    end_angle_value = 180 - (percentage / 100 * 180)
    theta_val = np.linspace(np.radians(start_angle), np.radians(end_angle_value), 100)
    x_outer_val = outer_radius * np.cos(theta_val)
    y_outer_val = outer_radius * np.sin(theta_val)
    x_inner_val = inner_radius * np.cos(theta_val)
    y_inner_val = inner_radius * np.sin(theta_val)
    
    # Draw blue value arc
    vertices_val = list(zip(x_outer_val, y_outer_val)) + list(zip(x_inner_val[::-1], y_inner_val[::-1]))
    polygon_val = patches.Polygon(vertices_val, facecolor=gauge_value_color, edgecolor='none')
    ax.add_patch(polygon_val)
    
    # Add scale markers
    scale_values = [0, 20, 40, 60, 80, 100]
    for val in scale_values:
        angle = 180 - (val / 100 * 180)
        angle_rad = np.radians(angle)
        
        # Position for text (outside the gauge)
        text_radius = outer_radius + 0.10
        x_text = text_radius * np.cos(angle_rad)
        y_text = text_radius * np.sin(angle_rad)
        
        ax.text(x_text, y_text, str(val), 
                ha='center', va='center', fontsize=10, color=scale_text_color)
    
    # Add center value 
    ax.text(0, 0.2, f'{percentage:.1f}%', 
            ha='center', va='center', fontsize=36, 
            fontweight='normal', color=text_color)
    
    # Add title with spacing
    ax.set_title('Sales Distribution by Product', 
                 pad=5, 
                 fontsize=12, 
                 fontweight='bold',
                 color=text_color)
    
    # Set background color
    fig.patch.set_facecolor(bg_color)
    
    return fig


def main():
    # Load data
    df = load_data()
    
    # Calculate total sales
    reported_sale = df["Sales"].iloc[0:8].sum()
    total_sales = df["Sales"].sum()

    # Create gauge chart with mode
    fig = create_gauge_chart(reported_sale, total_sales, "PERFORMANCE", mode=MODE)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the figure to output folder
    OUTPUT_FILE = Path("output") / f"gaugechart_{MODE}.png"
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    
    # Get background color for saving
    bg_color = '#1e1e1e' if MODE == 'dark' else 'white'
    plt.savefig(OUTPUT_FILE, dpi=150, bbox_inches='tight', facecolor=bg_color)
    print(f"Gauge chart saved to: {OUTPUT_FILE} ({MODE} mode)")
    
    # Show chart
    plt.show()

if __name__ == "__main__":
    main()