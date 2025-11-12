import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
data = pd.read_csv('C:/IDE/домашка матем/asset-v1_skillfactory+MIFIML-1sem+2025+type@asset+block@Математическии__анализ_и_теория_вероятностеи_._ДЗ_1._Данные_по_заданию_3 (2).txt')

print("Первые 5 строк данных:")
print(data.head())
print(f"\nРазмерность данных: {data.shape}")
print(f"\nИнформация о данных:")
print(data.info())
print(f"\nСтатистика данных:")
print(data.describe())


# 1. ФОРМАЛИЗАЦИЯ ЗАДАЧИ ЛИНЕЙНОЙ РЕГРЕССИИ


"""
Задача: предсказать Performance Index на основе признаков:
- Hours Studied
- Previous Scores  
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

Модель: y = w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + ε
где y - Performance Index (целевая переменная)
"""


# 2. ПРЕДОБРАБОТКА ДАННЫХ


# Проверка на пропуски
print(f"\nПропуски в данных:")
print(data.isnull().sum())

# Кодирование категориальной переменной
le = LabelEncoder()
data['Extracurricular Activities_encoded'] = le.fit_transform(data['Extracurricular Activities'])

# Разделение на признаки и целевую переменную
X = data[['Hours Studied', 'Previous Scores', 'Extracurricular Activities_encoded', 
          'Sleep Hours', 'Sample Question Papers Practiced']]
y = data['Performance Index']

# Нормализация данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Добавление столбца единиц для intercept (w0)
X_with_intercept = np.c_[np.ones(X_scaled.shape[0]), X_scaled]

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X_with_intercept, y, test_size=0.2, random_state=42
)

print(f"\nРазмеры выборок:")
print(f"Обучающая: {X_train.shape}, {y_train.shape}")
print(f"Тестовая: {X_test.shape}, {y_test.shape}")


# 3. РЕАЛИЗАЦИЯ ФУНКЦИИ ОШИБОК (MSE)


def compute_cost(X, y, theta):
    """
    Вычисление функции стоимости (MSE)
    
    Parameters:
    X - матрица признаков (m x n)
    y - вектор целевых значений (m x 1)
    theta - вектор параметров (n x 1)
    
    Returns:
    cost - значение функции стоимости
    """
    m = len(y)
    predictions = X.dot(theta)
    errors = predictions - y
    cost = (1/(2*m)) * np.sum(errors**2)
    return cost


# 4. РЕАЛИЗАЦИЯ ГРАДИЕНТНОГО СПУСКА


def gradient_descent(X, y, theta, alpha, num_iters):
    """
    Реализация градиентного спуска
    
    Parameters:
    X - матрица признаков
    y - вектор целевых значений
    theta - начальные параметры
    alpha - скорость обучения
    num_iters - количество итераций
    
    Returns:
    theta - оптимизированные параметры
    cost_history - история стоимости
    """
    m = len(y)
    cost_history = np.zeros(num_iters)
    
    for i in range(num_iters):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1/m) * X.T.dot(errors)
        theta = theta - alpha * gradient
        cost_history[i] = compute_cost(X, y, theta)
        
    return theta, cost_history

# Инициализация параметров
np.random.seed(42)
initial_theta = np.random.randn(X_train.shape[1])
alpha = 0.01
num_iters = 1000

print(f"\nНачальные параметры: {initial_theta}")

# Обучение модели
theta, cost_history = gradient_descent(X_train, y_train.values, initial_theta, alpha, num_iters)

print(f"\nОптимизированные параметры:")
feature_names = ['Intercept', 'Hours Studied', 'Previous Scores', 
                'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']
for name, param in zip(feature_names, theta):
    print(f"{name}: {param:.4f}")


# 5. АНАЛИЗ МОДЕЛИ И ПРЕДСКАЗАНИЯ


# Функция для предсказаний
def predict(X, theta):
    return X.dot(theta)

# Предсказания на тестовой выборке
y_pred_custom = predict(X_test, theta)

# Оценка точности
mse_custom = compute_cost(X_test, y_test.values, theta) * 2  # Умножаем на 2, т.к. у нас была 1/(2m)
r2_custom = 1 - (np.sum((y_test - y_pred_custom)**2) / np.sum((y_test - np.mean(y_test))**2))

print(f"\nРезультаты собственной реализации:")
print(f"MSE: {mse_custom:.4f}")
print(f"R²: {r2_custom:.4f}")

###########################################################
# 6. Обучение модели sklearn
lr_sklearn = LinearRegression()
lr_sklearn.fit(X_train[:, 1:], y_train)  # Исключаем столбец единиц

# Предсказания sklearn
y_pred_sklearn = lr_sklearn.predict(X_test[:, 1:])

# Оценка точности sklearn
mse_sklearn = mean_squared_error(y_test, y_pred_sklearn)
r2_sklearn = r2_score(y_test, y_pred_sklearn)

print(f"\nРезультаты sklearn:")
print(f"MSE: {mse_sklearn:.4f}")
print(f"R²: {r2_sklearn:.4f}")



# Сравнение коэффициентов
sklearn_coef = np.concatenate([[lr_sklearn.intercept_], lr_sklearn.coef_])
print(f"\nСравнение коэффициентов:")
print("Параметр\tСобственная\tSklearn\t\tРазница")
for i, (name, custom, sklearn) in enumerate(zip(feature_names, theta, sklearn_coef)):
    diff = abs(custom - sklearn)
    print(f"{name}\t\t{custom:.4f}\t\t{sklearn:.4f}\t\t{diff:.4f}")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))


    
# 7. ВЫВОДЫ
print(f"   - Собственная реализация: R² = {r2_custom:.4f}, MSE = {mse_custom:.4f}")
print(f"   - Sklearn: R² = {r2_sklearn:.4f}, MSE = {mse_sklearn:.4f}")
print(f"\n СРАВНЕНИЕ С БИБЛИОТЕЧНЫМ РЕШЕНИЕМ:")
max_diff = np.max(np.abs(theta - sklearn_coef))
print(f"   - Максимальная разница в коэффициентах: {max_diff:.6f}")

print(f"\n ИНТЕРПРЕТАЦИЯ КОЭФФИЦИЕНТОВ:")
print(f"   - Intercept (w0): {theta[0]:.4f} - базовый уровень Performance Index")
print(f"   - Hours Studied: {theta[1]:.4f} - увеличение на 1 std приводит к изменению на {theta[1]:.4f}")
print(f"   - Previous Scores: {theta[2]:.4f} - наиболее важный признак")
print(f"   - Extracurricular Activities: {theta[3]:.4f} - положительное влияние")
print(f"   - Sleep Hours: {theta[4]:.4f} - умеренное положительное влияние")  
print(f"   - Sample Question Papers: {theta[5]:.4f} - слабое положительное влияние")

