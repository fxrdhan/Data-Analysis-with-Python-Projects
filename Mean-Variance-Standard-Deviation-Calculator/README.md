# [Mean Variance Standard Deviation Calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

Welcome to the **Mean Variance Standard Deviation Calculator** project! This project focuses on performing essential statistical calculations using a 3 x 3 matrix and Python's powerful Numpy library.

## Overview

The primary goal of this project is to create a function named `calculate()` that computes key statistics—such as mean, variance, standard deviation, max, min, and sum—across the rows, columns, and the entire matrix. By leveraging Numpy, we can efficiently transform a list of numbers into a matrix and perform these calculations in a streamlined way.

## Tasks

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

- **Input:** A list containing 9 numerical elements.
- **Output:** A dictionary that presents the mean, variance, standard deviation, max, min, and sum of the elements calculated along the rows, columns, and the entire matrix.

For example, calling `calculate([0,1,2,3,4,5,6,7,8])` will give a comprehensive overview of these statistics in an organized format.

### Example Output

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

- **`mean_var_std.py`**: The core module where the `calculate()` function is defined.
- **`main.py`**: A simple script to run and test the `calculate()` function.
- **`test_module.py`**: Unit tests to ensure that the `calculate()` function works as expected.
- **`requirements.txt`**: A list of dependencies for this project, mainly including Numpy.

### Testing result
```bash
{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611], 'max': [[6, 7, 8], [2, 5, 8], 8], 'min': [[0, 1, 2], [0, 3, 6], 0], 'sum': [[9, 12, 15], [3, 12, 21], 36]}
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

## Project Link

You can view the project I have developed and its implementation at the following Replit link:

[View My Project on Replit](https://replit.com/@fxrdhan/Mean-Variance-Standard-Deviation-Calculator?v=1)

## Important Note

THIS PROJECT IS A PERSONAL PROJECT CREATED FOR CERTIFICATION PURPOSES AND SHOULD NOT BE SHARED, FORKED, OR USED BY OTHERS. PLEASE RESPECT THE PRIVACY AND CONFIDENTIALITY OF THIS WORK.
