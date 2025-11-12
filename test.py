from sympy import *


# Определяем символы
x, y, w = symbols('x y w')

# Целевая ф
f_target = 4*x + 8*y
print('Целевая функция: f =', f_target)

# Ф ограничений
constraint = y**2 - 2*x*y + 5
print('Ограничение:', constraint, '= 0')

# Ф Лагранжа
L = 4*x + 8*y + w*(y**2 - 2*x*y + 5)
print('Функция Лагранжа: L =', L)

# Частные производные
L_x = L.diff(x)
print('∂L/∂x =', L_x, '= 0')

L_y = L.diff(y)
print('∂L/∂y =', L_y, '= 0')

L_w = L.diff(w)
print('∂L/∂w =', L_w, '= 0')

# Решение системы
solutions = solve([L_x, L_y, L_w], [x, y, w])
print('\nСтационарные точки:')

# Вывод результата
for i, sol in enumerate(solutions, 1):
    print(f'Точка {i}: x = {sol[0]}, y = {sol[1]}, w = {sol[2]}')
    print(f'f(x, y) = {4*sol[0] + 8*sol[1]}')
