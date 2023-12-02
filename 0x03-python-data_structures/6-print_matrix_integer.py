#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(0, len(matrix)):
        print("{}".format(matrix[i]).replace("[", "").replace("]", ""))
