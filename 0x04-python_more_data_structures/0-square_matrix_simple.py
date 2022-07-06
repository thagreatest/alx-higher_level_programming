#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append([pow(y, 2) for y in i])
    return new_matrix
