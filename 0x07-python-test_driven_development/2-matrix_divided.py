#!/usr/bin/python3
"""
Program to divide a matrix
"""


def matrix_divided(matrix, div):
    """function to divide elements of matrix by div"""
    al = all(isinstance(j, (float, int)) for i in matrix for j in i)
    vld = isinstance(matrix, list) and all(isinstance(r, list) for r in matrix)
    same_size = all(len(row) == len(matrix[0]) for row in matrix)
    if not (al and vld):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not same_size:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix = [[round(x/div, 2) for x in r] for r in matrix]
    return matrix
