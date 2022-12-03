#!/usr/bin/phyton3
#print_matrix_integer:prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("")
