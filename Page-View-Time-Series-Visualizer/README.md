# [Page View Time Series Visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer)

Welcome to the **Page View Time Series Visualizer** project! This project focuses on visualizing time series data related to page views on the freeCodeCamp.org forum over a specified period. Using Python libraries such as Pandas, Matplotlib, and Seaborn, the goal is to create line charts, bar charts, and box plots that help illustrate trends in the data.

## Overview

The dataset represents daily page views on the freeCodeCamp.org forum from **2016-05-09** to **2019-12-03**. Through this visualization, we aim to understand trends in visits over time and analyze the data both annually and monthly.

## Completed Tasks

In this project, I have completed the following tasks:

1. **Import Data**: Imported the data using Pandas from `fcc-forum-pageviews.csv` and set the index to the date column.
2. **Clean the Data**: Filtered the dataset by removing data points where page views fall into the top or bottom 2.5%, ensuring a focus on typical usage patterns.
3. **Draw Line Plot**: Created the function `draw_line_plot` using Matplotlib to generate a line chart. This chart visualizes daily page views with the title "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", labeling the x-axis as "Date" and the y-axis as "Page Views".
4. **Draw Bar Plot**: Developed the `draw_bar_plot` function to create a bar chart that displays the average daily page views for each month, grouped by year. The x-axis represents "Years", and the y-axis shows "Average Page Views". The legend categorizes the bars by month.
5. **Draw Box Plot**: Implemented the `draw_box_plot` function using Seaborn to generate two adjacent box plots. These plots show the distribution of page views per year and per month, helping to highlight trends and seasonal variations. The first plot is titled "Year-wise Box Plot (Trend)" and the second is titled "Month-wise Box Plot (Seasonality)".

For each chart, I ensured that a copy of the data frame is used to avoid modifying the original data.

## Files in This Project

- **`time_series_visualizer.py`**: Core script for generating all visualizations based on the time series data.
- **`main.py`**: A script to run and test the functions in `time_series_visualizer.py`.
- **`test_module.py`**: Unit tests to ensure the visualizations and calculations produce the expected results.
- **`fcc-forum-pageviews.csv`**: The dataset file containing daily page views data.
- **`requirements.txt`**: A list of dependencies required for the project, including Pandas, Matplotlib, and Seaborn.
- **Output Files**: This project generates visual outputs saved as PNG files:
  - `line_plot.png`: Line chart showing daily page views over time.
    ![image](https://github.com/user-attachments/assets/67c71a4f-8f2b-4890-9a52-3e804814d513)
  - `bar_plot.png`: Bar chart visualizing average page views per month, grouped by year.
    ![image](https://github.com/user-attachments/assets/dbd0076c-0957-452f-a8fd-8d33ae5f2037)
  - `box_plot.png`: Box plots illustrating trends and seasonal variations in page views.
    ![image](https://github.com/user-attachments/assets/affd2d2c-59f7-43e7-b2fb-c094861c63e5)

### Testing result
```bash
...........
----------------------------------------------------------------------
Ran 11 tests in 3.392s

OK
```

## Project Link

You can view the implementation of this project at the following Replit link:

[View My Project on Replit](https://replit.com/@fxrdhann/Page-View-Time-Series-Visualizer?v=1)

## Important Note

THIS PROJECT IS A PERSONAL PROJECT CREATED FOR CERTIFICATION PURPOSES AND SHOULD NOT BE SHARED, FORKED, OR USED BY OTHERS. PLEASE RESPECT THE PRIVACY AND CONFIDENTIALITY OF THIS WORK.
