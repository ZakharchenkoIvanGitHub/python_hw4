"""Напишите функцию для транспонирования матрицы"""


def print_matrix(matrix: list):
    for el in matrix:
        print(*el)


def transport_matrix(matrix: list) -> list:
    rows = len(m)
    columns = len(m[0])
    new_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
    for ind1 in range(rows):
        for ind2 in range(columns):
            new_matrix[ind2][ind1] = matrix[ind1][ind2]
    return new_matrix


def transport_matrix_zip(matrix: list) -> list:
    return list(zip(*matrix))


m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
print_matrix(m)

print()
m2 = transport_matrix(m)
print_matrix(m2)

print()
m3 = transport_matrix_zip(m)
print_matrix(m3)
