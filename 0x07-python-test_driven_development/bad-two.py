#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not all(isinstance(member, list) for member in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
    for i in range(len(matrix)):
        for element in i:
            if type(element) != int and type(element) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
    lengthy = len(matrix[0])
    for member in matrix:
        if len(member) != lengthy:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [row[:] for row in matrix]
    
    
