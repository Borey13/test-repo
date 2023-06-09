import random

n = 5
matrix = [[random.randint(0, 100) for i in range(n)] for j in range(n)]

for i in range(n):
    print(matrix[i])

#                                       Вариант 1

list_max = []

for i in range(n):
    list_max.append(max(matrix[i]))

print("Максимальный элемент матрицы равен:", max(list_max), "(Первый вариант решения задачи)")

#                                       Вариант 2

max_elem = matrix[0][0]

for i in range(n):
    for j in range(n):
        if max_elem < matrix[i][j]:
            max_elem = matrix[i][j]

print("Максимальный элемент матрицы равен:", max_elem, "(Второй вариант решения задачи)")
