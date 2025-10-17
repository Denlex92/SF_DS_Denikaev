import numpy as np
from scipy.optimize import linear_sum_assignment

# Матрица стоимостей
cost = np.array([
    [1000, 12, 10, 19, 8],
    [12, 1000, 3, 7, 2],
    [10, 3, 1000, 6, 20],
    [19, 7, 6, 1000, 4],
    [8, 2, 20, 4, 1000]
])

# Венгерский алгоритм ищет минимальную стоимость
row_ind, col_ind = linear_sum_assignment(cost)

# Суммируем стоимость оптимальных назначений
total_cost = cost[row_ind, col_ind].sum()

print("Оптимальные назначения (исполнитель -> задача):")
for i, j in zip(row_ind, col_ind):
    print(f"Исполнитель {i+1} -> Задача {j+1} (стоимость {cost[i, j]})")

print(f"\nМинимальная суммарная стоимость: {total_cost}")
#добавим на гит