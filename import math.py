import math

# Данные
n = 10000 #число ноутбуков
p = 0.0002 #вероятность поломки одного ноутбука в течении мес
laptop_price = 500 #стоимость ремонта или замены ноутбука

print(f"n = {n}, p = {p}")

# Ожидаемое число событий за период времени
lambda_poisson = n * p
print(f"\n1. Ожидаемое число событий за период времени:")
print(f"λ = n × p = {n} × {p} = {lambda_poisson}")

# Вопрос 1: Вероятность, что сломается ровно 1 ноутбук
print(f"\n2. ВОПРОС 1: Вероятность, что сломается ровно 1 ноутбук")
print(f"Формула Пуассона: P(X=k) = (λ^k × e^(-λ)) / k!")
print(f"P(X=1) = ({lambda_poisson}^1 × e^(-{lambda_poisson})) / 1!")

e_lambda = math.exp(-lambda_poisson)
P_X1 = (lambda_poisson ** 1) * e_lambda / math.factorial(1)
print(f"P(X=1) = ({lambda_poisson} × {e_lambda:.6f}) / 1 = {P_X1:.6f}")
print(f"Ответ: P(X=1) ≈ {P_X1:.3f}")

# Вопрос 2а: Вероятность, что сломается более 5 ноутбуков
print(f"\n3. ВОПРОС 2а: Вероятность, что сломается более 5 ноутбуков")
print(f"P(X>5) = 1 - P(X≤5)")
print(f"P(X≤5) = Σ P(X=k) для k=0 до 5")

# Вычисляем каждую вероятность аналитически(из 1 вычитаем сумму вероятностей поломки 0+1+2+3+4+5 ноутбуков)
probabilities = []
for k in range(0, 6):
    P_k = (lambda_poisson ** k) * e_lambda / math.factorial(k)
    probabilities.append(P_k)
    print(f"P(X={k}) = {P_k:.6f}")

P_X_leq_5 = sum(probabilities)
P_X_gt_5 = 1 - P_X_leq_5

print(f"\nP(X≤5) = {P_X_leq_5:.6f}")
print(f"P(X>5) = 1 - {P_X_leq_5:.6f} = {P_X_gt_5:.6f}")
print(f"Ответ: P(X>5) ≈ {P_X_gt_5:.4f}")

# Вопрос 2б: Математическое ожидание расходов
print(f"\n4. ВОПРОС 2б: Математическое ожидание расходов")
print(f"E[количество поломок] = λ = {lambda_poisson}")
print(f"Стоимость ремонта одного ноутбука = {laptop_price} долларов")
print(f"E[расходы] = E[количество поломок] × стоимость ремонта")
expected_cost = lambda_poisson * laptop_price
print(f"E[расходы] = {lambda_poisson} × {laptop_price} = {expected_cost} долларов")

print(f"\n5. ИТОГОВЫЕ ОТВЕТЫ:")
print(f"1. P(X=1) ≈ {P_X1:.3f}")
print(f"2а. P(X>5) ≈ {P_X_gt_5:.4f}")
print(f"2б. Математическое ожидание расходов = {expected_cost} долларов")

print(f"\nSCIPY")

import scipy.stats as stats

poisson_dist = stats.poisson(lambda_poisson)
P_X1_check = poisson_dist.pmf(1)
P_X_gt_5_check = 1 - poisson_dist.cdf(5)

print(f"P(X=1) проверка: {P_X1_check:.6f}")
print(f"P(X>5) проверка: {P_X_gt_5_check:.6f}")
print(f"Расхождения: {abs(P_X1 - P_X1_check):.2e}, {abs(P_X_gt_5 - P_X_gt_5_check):.2e}")