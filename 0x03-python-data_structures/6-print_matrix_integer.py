#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return
    for i in matrix:
        if not i:
            continue
        print("{:d}".format(i[0]), end="")
        for j in i[1:]:
            print(" {:d}".format(j), end="")
        print("")
