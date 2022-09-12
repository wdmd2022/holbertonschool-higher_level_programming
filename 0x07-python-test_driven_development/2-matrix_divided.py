#!/usr/bin/python3
"""this module contains a function to divide a matrix.
"""


def matrix_divided(matrix, div):
    """this function divides a matrix

    Args:
        matrix (list): a list of lists of floats or ints
        div (int or float): number to divide everything by

    Raises:
        TypeError: if matrix is not a list
        TypeError: if each member of matrix is not a list
        TypeError: if the lists are of different sizes
        TypeError: if the members of each sublist are not ints/floats
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero

    Returns:
        _type_: _description_
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for member in matrix:
        if type(member) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(member) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in member:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [x[:] for x in matrix]
    for newmember in newmatrix:
        for newi in range(len(newmember)):
            newmember[newi] = round(newmember[newi] / div, 2)
    return newmatrix
