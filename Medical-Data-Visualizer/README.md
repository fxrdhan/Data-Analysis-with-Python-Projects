# [Medical Data Visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)

Welcome to the **Medical Data Visualizer** project! This project involves visualizing and analyzing medical examination data using Python libraries like matplotlib, seaborn, and pandas.

## Overview

The dataset contains information collected from medical examinations, including body measurements, blood test results, and lifestyle choices. The goal is to explore the relationships between these variables and cardiovascular disease.

## Data Description

The rows in the dataset represent patients, and the columns represent various attributes, such as body measurements, blood markers, and lifestyle choices.

**File name**: `medical_examination.csv`

| Feature                        | Variable Type         | Variable            | Value Type                      |
|--------------------------------|-----------------------|---------------------|---------------------------------|
| Age                            | Objective Feature     | age                 | int (days)                      |
| Height                         | Objective Feature     | height              | int (cm)                        |
| Weight                         | Objective Feature     | weight              | float (kg)                      |
| Gender                         | Objective Feature     | gender              | categorical code                |
| Systolic blood pressure        | Examination Feature   | ap_hi               | int                             |
| Diastolic blood pressure       | Examination Feature   | ap_lo               | int                             |
| Cholesterol                    | Examination Feature   | cholesterol         | 1: normal, 2: above normal, 3: well above normal |
| Glucose                        | Examination Feature   | gluc                | 1: normal, 2: above normal, 3: well above normal |
| Smoking                        | Subjective Feature    | smoke               | binary                          |
| Alcohol intake                 | Subjective Feature    | alco                | binary                          |
| Physical activity              | Subjective Feature    | active              | binary                          |
| Presence or absence of cardiovascular disease | Target Variable | cardio              | binary                          |

## Completed Tasks

In this project, I have completed the following tasks:

1. Imported the data from `medical_examination.csv` and assigned it to the `df` variable.
2. Created a new `overweight` column in the DataFrame based on the BMI of the patients.
3. Adjusted the `cholesterol` and `gluc` values by normalizing them such that a value of 1 is changed to 0, and any value greater than 1 is changed to 1.
4. Defined the function `draw_cat_plot` to generate a categorical plot that visualizes various health metrics in relation to cardiovascular disease.
5. Transformed the data into a long format using `pd.melt` for the categorical plot, focusing on columns like `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight`.
6. Grouped the data in `df_cat` by the `cardio` feature, adjusted the formatting for the categorical plot, and displayed the counts of each category.
7. Used `sns.catplot()` to plot the data, showing the counts for each feature split by cardiovascular status.
8. Extracted the resulting figure and stored it in the `fig` variable for further output.
9. Kept the following lines intact to ensure the correct output: `fig.savefig('catplot.png')`.
10. Created the `draw_heat_map` function to generate a heatmap of correlations among the features.
11. Cleaned the data in `df_heat` by filtering out rows where the diastolic blood pressure (`ap_lo`) is higher than the systolic (`ap_hi`). Additionally, filtered out rows where height and weight values fall outside the 2.5th and 97.5th percentiles.
12. Calculated the correlation matrix of the cleaned DataFrame and stored it in the `corr` variable.
13. Created a mask for the upper triangle of the heatmap to avoid displaying duplicate values.
14. Initialized a matplotlib figure for plotting the heatmap.
15. Used the `sns.heatmap()` function to plot the correlation matrix with appropriate annotations.
16. Preserved the following line to save the heatmap: `fig.savefig('heatmap.png')`.

## Files in This Project

- **`medical_data_visualizer.py`**: Core script for performing data analysis and generating visualizations.
- **`main.py`**: A script to run and test the `medical_data_visualizer.py` calculations.
- **`test_module.py`**: Unit tests to ensure that the visualizations and calculations are correct.
- **`medical_examination.csv`**: The dataset file containing medical examination data.
- **`requirements.txt`**: A list of dependencies for this project, mainly including matplotlib, seaborn, and pandas.
- **Output Files**: This project generates visual outputs saved as PNG files:
  - `catplot.png`: Categorical plot visualizing various factors.
    <br></br>
    ![image](https://github.com/user-attachments/assets/fd0ddb05-178d-4a64-9d0f-2402c1746240)

  - `heatmap.png`: Heatmap showing correlations between features.
    <br></br>
    ![image](https://github.com/user-attachments/assets/dc08e71b-d6c8-4300-8aaa-2f12445d7db0)

 
### Testing result
```bash
...['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
.
----------------------------------------------------------------------
Ran 4 tests in 2.576s

OK
```

## Project Link

You can view the project I have developed and its implementation at the following Replit link:

[View My Project on Replit](https://replit.com/@fxrdhan/Medical-Data-Visualizer?v=1)

## Dataset Source

Dua, D. and Graff, C. (2019). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science.

## Important Note

THIS PROJECT IS A PERSONAL PROJECT CREATED FOR CERTIFICATION PURPOSES AND SHOULD NOT BE SHARED, FORKED, OR USED BY OTHERS. PLEASE RESPECT THE PRIVACY AND CONFIDENTIALITY OF THIS WORK.
