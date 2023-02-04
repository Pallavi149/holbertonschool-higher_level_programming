#!/usr/bin/python3
""" This is module provide function 'matrix_divided' """


def matrix_divided(matrix, div):
    """ This function returns a matrix where
    each item in matrix is divided by value
    """
    typeError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(typeError)
    result = []
    for i in range(len(matrix)):
        row = matrix[i]
        rowResult = []
        if not isinstance(row, list):
            raise TypeError(typeError)
        length = len(row)
        if len(matrix[0]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(length):
            element = row[j]
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(typeError)
            rowResult.append(round(element/div, 2))
        result.append(rowResult)
    return result
