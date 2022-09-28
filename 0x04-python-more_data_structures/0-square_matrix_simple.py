#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for j in range(len(matrix)):
        new_matrix[j] = list(map(lambda x: x**2, matrix[j]))

    return (new_matrix)
