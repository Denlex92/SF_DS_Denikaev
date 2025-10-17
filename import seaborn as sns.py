import numpy as np
from scipy.optimize import linprog

c = [2, 5, 3, 7, 7, 6]  # коэффициенты целевой функции

# Ограничения-равенства:
A_eq = [
    [1, 1, 1, 0, 0, 0],  # склад 1
    [0, 0, 0, 1, 1, 1],  # склад 2
    [1, 0, 0, 1, 0, 0],  # ТЦ1
    [0, 1, 0, 0, 1, 0],  # ТЦ2
    [0, 0, 1, 0, 0, 1]   # ТЦ3
]
b_eq = [180, 220, 110, 150, 140]

# Решаем задачу минимизации
res = linprog(c, A_eq=A_eq, b_eq=b_eq, method='highs')

print("Статус:", res.message)
print("Оптимальный план:")
print(f"x11 = {res.x[0]}, x12 = {res.x[1]}, x13 = {res.x[2]}")
print(f"x21 = {res.x[3]}, x22 = {res.x[4]}, x23 = {res.x[5]}")
print("Минимальная стоимость:", round(res.fun))