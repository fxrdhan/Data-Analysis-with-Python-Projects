# [Sea Level Predictor](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)

Welcome to the **Sea Level Predictor** project! This project focuses on analyzing historical data related to sea level changes and using statistical methods to predict future sea levels through 2050.

## Overview

The dataset includes global average sea level changes since **1880**. The objective is to visualize this data, analyze trends, and make predictions about future sea levels using Python libraries like Pandas, Matplotlib, and Scipy.

## Completed Tasks

In this project, I have completed the following tasks:

1. **Import Data**: Loaded the data from `epa-sea-level.csv` using Pandas for analysis.
2. **Create Scatter Plot**: Created a scatter plot with the `Year` on the x-axis and `CSIRO Adjusted Sea Level` on the y-axis to visualize sea level changes over time.
3. **Line of Best Fit (Full Dataset)**: Used the `linregress` function from `scipy.stats` to calculate the slope and intercept of a line of best fit using all available data. Extended this line through the year 2050 to predict future sea level rise.
4. **Line of Best Fit (Since 2000)**: Developed a second line of best fit using data from the year **2000** onwards, extending it through the year **2050**. This provides an alternate prediction based on more recent trends.
5. **Labels and Title**: Added labels for the x-axis ("Year") and y-axis ("Sea Level (inches)") and set the chart title to "Rise in Sea Level".

## Files in This Project

- **`sea_level_predictor.py`**: The core script for analyzing the data, creating visualizations, and making predictions.
- **`main.py`**: A script to run and test the `sea_level_predictor.py` functions.
- **`test_module.py`**: Unit tests to verify that the visualizations and calculations are correct.
- **`epa-sea-level.csv`**: The dataset file containing the historical sea level data.
- **`requirements.txt`**: A list of dependencies, including Pandas, Matplotlib, and Scipy.
- **Output Files**: This project generates visual outputs saved as PNG files:
  - `sea_level_plot.png`: A plot that shows the scatter plot and both lines of best fit, extending through 2050.
    ![image](https://github.com/user-attachments/assets/873fd7b6-ebc7-44ea-a115-7bd10d3d12a5)

### Testing result
```bash
....
----------------------------------------------------------------------
Ran 4 tests in 0.979s

OK
```

## Project Link

You can view the details and code implementation of this project at the following Replit link:

[View My Project on Replit](https://replit.com/@fxrdhann/Sea-Level-Predictor?v=1)

## Data Source

[Global Average Absolute Sea Level Change](https://datahub.io/core/sea-level-rise), 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

## Important Note

THIS PROJECT IS A PERSONAL PROJECT CREATED FOR CERTIFICATION PURPOSES AND SHOULD NOT BE SHARED, FORKED, OR USED BY OTHERS. PLEASE RESPECT THE PRIVACY AND CONFIDENTIALITY OF THIS WORK.
