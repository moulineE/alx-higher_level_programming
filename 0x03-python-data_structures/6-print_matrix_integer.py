#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i > 0:
            print()
        for y in range(len(matrix[0])):
            if y == len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][y]), end="")
                continue
            print("{:d}".format(matrix[i][y]), end=" ")
    print()
