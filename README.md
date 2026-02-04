# Python Charts

## Bar Charts
Bar charts are ideal for comparing values across categories, such as sales by region or product type. It clearly shows differences
between groups, making it useful for visualizing rankings, distributions, or changes over time with discrete data.

![Bar Chart](output/barchart.png)

## Horizontal Bar Charts
Horizontal bar charts are ideal when you need to display categorical data with long labels, many categories, or ranked items, as they enhance readability and make comparisons between categories easier.

![Horizontal Bar Chart](output/hbarchart.png)

## Pie Charts
A pie charts are ideal for showing how parts make up a whole. It's best used with a small number of categories to display percentage or proportional data, such as market share or budget breakdowns, where the total equals 100%.

![Pie Chart](output/piechart.png)

## Donut Charts
Donut charts are used to represent parts of a whole while improving clarity in data visualization and allowing more effective use of space for labels or additional information.

![Donut Chart](output/donutchart.png)

## Line Charts
A line chart is ideal for showing trends over time or continuous data. It helps visualize patterns, increases, or decreases across
time intervals, such as monthly sales, temperature changes, or stock prices. It's best when the data points are connected sequentially.

![Line Charts](output/linechart.png)

## Scatter Plot Charts
Scatter plots charts are ideal for showing relationships or correlations between two numeric variables. They help identify patterns, trends, clusters, or outliers, such as height vs. weight or sales vs. advertising spend, making them perfect for exploring data distributions and dependencies.

![Scatter Plot Charts](output/scatterplotchart.png)

## Gauge Charts
Gauge charts are used to quickly visualize a single measure against a scale, making them ideal for tracking performance, KPIs, or progress toward goals.

![Gauge Charts](output/gaugechart.png)


## U.S.A. Map
Visualizing database data on a map helps reveal geographic patterns, trends, and insights that are difficult to see in raw tables. The right visualization type depends on your data structure and the story you want to tell.

![USA Charts](output/us_population_map.png)


## Features
- **Automated Data Loading**: Reads sales data from a structured CSV file
- **Chronological Ordering**: Ensures months are displayed in correct calendar order
- **Color-Coded Visualization**: Uses a blue gradient to represent sales magnitude
- **Clean Design**: Includes gridlines, labels, and professional styling
- **Error Handling**: Validates file existence before processing


## Requirements
```txt
pandas
seaborn
matplotlib
pathlib
```


## Project Structure
```
project/
│
├── data/
│   └── sales_data.csv    # Sales data file
│
├── barchart.py         # barchart script
├── linechart.py        # linechart script
├── piechart.py         # piechart script
├── scatterplotchart.py # scatterplotchart script
└── README.md     # This file
```