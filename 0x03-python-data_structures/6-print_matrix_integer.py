#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix) - 1
    if n == 0:
        print('')
    else:
        for i in range(0, len(matrix)):
            print("")
            for j in range(0, len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end= ' ')
    print("")
