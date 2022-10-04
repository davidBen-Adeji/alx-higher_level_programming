#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    length = len(matrix)

    for i in range(length):
        length_1 = len(matrix[i])
        if length_1 == 0:
            print(" ")
            continue

        for j in range(length_1):
            if j + 1 == length_1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
