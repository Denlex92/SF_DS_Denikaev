
import numpy as np

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

# Индексы NaN значений
nans_index = np.isnan(mystery)

# Количество NaN
n_nan = np.sum(nans_index)  # или n_nan = len(mystery[nans_index])

# Создаем копию массива и заменяем NaN на 0
mystery_new = mystery.copy()
mystery_new[np.isnan(mystery_new)] = 0

# Преобразуем в целочисленный тип
mystery_int = mystery_new.astype(np.int32)

# Сортируем массив
array = np.sort(mystery_int)

# Создаем таблицу 5x3 с заполнением по столбцам
table = array.reshape((5, 3), order='F')