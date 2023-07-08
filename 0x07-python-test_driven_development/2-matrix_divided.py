#!/usr/bin/python3
"""This module define a fonction
that divides all elements of a matrix
matrix must be a list of lists of integers or floats
div must be a number (integer or float)
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (list): a list of lists of integers or floats
        div (int, float): the divisor that must be a number

    Returns:
        a matrix with all the divided element of the first matrix

    Raises:
        TypeError: if matix containe non int or float
        TypeError: if row of the matrix must have the same size
        TypeError: id div is no an int or a float
        ZeroDivisionError: is div == 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all((isinstance(digit, int) or isinstance(digit, float))
                    for digit in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
