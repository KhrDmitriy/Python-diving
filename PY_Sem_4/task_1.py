# 1. Напишите функцию для транспонирования матрицы .

matrix = [[1, 2], [4, 5], [7, 8]]


def my_transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


print(my_transpose(matrix))
