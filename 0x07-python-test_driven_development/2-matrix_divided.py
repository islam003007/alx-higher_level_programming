#!/usr/bin/python3
"""divides all elements of a fucntion"""


def matrix_divided(matrix, div):
    """devides all elements of a function"""

    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_length = len(matrix[0])

    if type(matrix) is not list:
        raise TypeError(type_error)

    for i in matrix:
        if type(i) is not list:
            raise TypeError(type_error)
        if len(i) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(type_error)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(round(j/div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
