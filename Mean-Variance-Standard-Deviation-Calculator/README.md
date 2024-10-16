# [Mean Variance Standard Deviation Calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

Welcome to the **Mean Variance Standard Deviation Calculator** project! This project focuses on performing essential statistical calculations using a 3 x 3 matrix and Python's powerful Numpy library.

## Overview

The primary goal of this project is to create a function named `calculate()` that computes key statistics—such as mean, variance, standard deviation, max, min, and sum—across the rows, columns, and the entire matrix. By leveraging Numpy, we can efficiently transform a list of numbers into a matrix and perform these calculations in a streamlined way.

## How It Works

- **Input:** A list containing 9 numerical elements.
- **Output:** A dictionary that presents the mean, variance, standard deviation, max, min, and sum of the elements calculated along the rows, columns, and the entire matrix.

For example, calling `calculate([0,1,2,3,4,5,6,7,8])` will give a comprehensive overview of these statistics in an organized format.

## Example Output

Here’s a sample output when the input is `[0,1,2,3,4,5,6,7,8]`:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.45, 2.45, 2.45], [0.82, 0.82, 0.82], 2.58],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Files in This Project

- `mean_var_std.py`: The core module where the `calculate()` function is defined.
- `main.py` A simple script to run and test the `calculate()` function.
- `test_module.py`: Unit tests to ensure that the `calculate()` function works as expected.
- `requirements.txt`: A list of dependencies for this project, mainly including Numpy.

## Getting Started

To run the project, use the following Replit environment:

[Run the Project on Replit](https://replit.com/@fxrdhan/Mean-Variance-Standard-Deviation-Calculator?v=1)

This will allow you to execute the code, test the `calculate()` function, and view the results directly in an online environment without the need to set up anything locally.

## Important Note

This project is a personal project created for certification purposes and should not be shared, forked, or used by others. Please respect the privacy and confidentiality of this work.
