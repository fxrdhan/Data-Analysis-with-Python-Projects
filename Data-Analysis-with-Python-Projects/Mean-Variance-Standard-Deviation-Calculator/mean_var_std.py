import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    mean_axis0 = np.mean(matrix, axis=0).tolist()
    mean_axis1 = np.mean(matrix, axis=1).tolist()
    mean_flattened = np.mean(matrix)

    var_axis0 = np.var(matrix, axis=0).tolist()
    var_axis1 = np.var(matrix, axis=1).tolist()
    var_flattened = np.var(matrix)

    std_axis0 = np.std(matrix, axis=0).tolist()
    std_axis1 = np.std(matrix, axis=1).tolist()
    std_flattened = np.std(matrix)

    max_axis0 = np.max(matrix, axis=0).tolist()
    max_axis1 = np.max(matrix, axis=1).tolist()
    max_flattened = np.max(matrix)

    min_axis0 = np.min(matrix, axis=0).tolist()
    min_axis1 = np.min(matrix, axis=1).tolist()
    min_flattened = np.min(matrix)

    sum_axis0 = np.sum(matrix, axis=0).tolist()
    sum_axis1 = np.sum(matrix, axis=1).tolist()
    sum_flattened = np.sum(matrix)

    calculations = {
        "mean": [mean_axis0, mean_axis1, mean_flattened],
        "variance": [var_axis0, var_axis1, var_flattened],
        "standard deviation": [std_axis0, std_axis1, std_flattened],
        "max": [max_axis0, max_axis1, max_flattened],
        "min": [min_axis0, min_axis1, min_flattened],
        "sum": [sum_axis0, sum_axis1, sum_flattened],
    }

    return calculations
