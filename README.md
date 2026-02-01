# Charts

## Bar Charts
A Python data visualization project that creates a bar chart displaying monthly sales performance with color-coded bars based on sales values.


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
├── barchart.py   # Main script
└── README.md     # This file
```