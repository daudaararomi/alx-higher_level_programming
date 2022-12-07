#!/usr/bin/python3
# Computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        square_matrix.append([x**2 for x in matrix[i]])
    return (square_matrix)
