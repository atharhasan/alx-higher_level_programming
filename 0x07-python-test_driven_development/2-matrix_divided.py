#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

    Args:
    matrix (list of lists): list of lists of int or float.
    div (int) : number interger or float.
    """
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(errorMessage)
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
