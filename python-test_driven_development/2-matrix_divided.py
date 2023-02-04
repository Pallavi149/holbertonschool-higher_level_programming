#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = None
    result = []
    for i in range(len(matrix)):
        row = matrix[i]
        rowResult = []
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if length == None:
            length = len(row)
        elif length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(length):
            element = row[j]
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            rowResult.append(element/div)
        result.append(rowResult)
    return result
