import scipy.stats as st

mean = 100
std = 4
n = 64
se = std / n**0.5

left = mean - st.norm.ppf(.975)*se
right = mean + st.norm.ppf(.975)*se
print(f"{left} {right}")
print(se)

a = [1, 5, 12, 15, 10]
sem = st.sem(a) # или для Генеральной st.sem(a, ddof=0)
print(sem) # se Стандартная ошибка среднего se = sd / sqrt(n)

# доверительный интервал   x_mean-se*1.96--------x_mean--------x_mean+se*1.96
# (95% что значение будет на данном интервале)
# (99% что значение будет на данном интервале - 2.58)

x_m = 10
sd = 5
n = 100
se = sd / n**0.5
print(f"{x_m-se*2.58} {x_m+se*2.58}")
# ===
import math
from scipy import stats
def confidence_interval(sd, X, N, target_interval):
    alpha = 1 - target_interval
    z = abs(stats.norm.ppf(alpha/2))
    se = sd / math.sqrt(N)
    return (round(X - z * se,  2),  round(X + z * se,  2))
print(confidence_interval(5, 10, 100, 0.99))
# ===
interval = lambda Sd, n, t: (Sd / 100 ** 0.5) * t
print(10 - interval(5, 100, 2.58), 10 + interval(5, 100, 2.58))

# 1. se = sd/n^0.5
# 2. P(вероятность) = 1 - (1 - %(доверительного интервала)/2
# 3. Смотрим значение в табличке для нашего P. Я использовал в EXCEL "НОРМ.СТ.ОБР()", в R - "qnorm()", в python - "scipy.stats.norm.ppf()"
# 4. Величина отклонения для среднего (пусть будет ds, я ХЗ как это называется) = 1й пункт(se) + 3й пункт(обратное значение стандартного нормального распределения).
# 5. Левая граница = x - ds . Правая граница = x + ds