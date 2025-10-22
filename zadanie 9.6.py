import numpy as np

# Задаем seed
np.random.seed(2021)

# 1. Случайное число в диапазоне от 0 до 1
simple = np.random.random()

# 2. 120 чисел в диапазоне от -150 до 2021
randoms = np.random.uniform(-150, 2022, size=120)

# 3. Массив 3x2 из случайных целых чисел от 1 до 100
table = np.random.randint(1, 101, size=(3, 2))

# 4. Четные числа от 2 до 16 (включительно)
even = np.arange(2, 17, 2)

# 5. Копируем even в mix и перемешиваем
mix = even.copy()
np.random.shuffle(mix)

# 6. Получаем 3 числа без повторений из even
select = np.random.choice(even, size=3, replace=False)

# 7. Получаем triplet - перемешанные значения из select (select не изменяется)
triplet = select.copy()
np.random.shuffle(triplet)

print(randoms)