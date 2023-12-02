#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(0, len(matrix)):
        print("")
        for j in range(0, len(matrix[i])):
            print("{}".format(matrix[i][j]), end= ' ')
    print("")
