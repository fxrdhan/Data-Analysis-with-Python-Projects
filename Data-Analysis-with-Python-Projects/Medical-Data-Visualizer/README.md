In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

### Data Description
The rows in the dataset represent patients, and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

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

### Instructions
By each number in the `medical_data_visualizer.py` file, add the code from the associated instruction number below.

1. **Import the Data**: Import the data from `medical_examination.csv` and assign it to the `df` variable.
2. **Create the Overweight Column**: Create the `overweight` column in the `df` variable.
3. **Normalize Data**: Normalize data by making 0 always good and 1 always bad. If the value of `cholesterol` or `gluc` is 1, set the value to 0. If the value is more than 1, set the value to 1.
4. **Draw the Categorical Plot**: In the `draw_cat_plot` function:
    - Create a DataFrame for the cat plot using `pd.melt` with values from `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight` in the `df_cat` variable.
    - Group and reformat the data in `df_cat` to split it by `cardio`. Show the counts of each feature. You will have to rename one of the columns for the `catplot` to work correctly.
    - Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: `sns.catplot()`.
    - Get the figure for the output and store it in the `fig` variable.
    - **Do not modify the next two lines**.
5. **Draw the Heat Map**: In the `draw_heat_map` function:
    - Clean the data in the `df_heat` variable by filtering out the following patient segments that represent incorrect data:
        - Diastolic pressure is higher than systolic (Keep the correct data with `(df['ap_lo'] <= df['ap_hi'])`).
        - Height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`).
        - Height is more than the 97.5th percentile.
        - Weight is less than the 2.5th percentile.
        - Weight is more than the 97.5th percentile.
    - Calculate the correlation matrix and store it in the `corr` variable.
    - Generate a mask for the upper triangle and store it in the `mask` variable.
    - Set up the matplotlib figure.
    - Plot the correlation matrix using the method provided by the seaborn library import: `sns.heatmap()`.
    - **Do not modify the next two lines**.
