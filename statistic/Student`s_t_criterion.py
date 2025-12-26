from scipy import stats
import numpy as np

a = np.array([84.7, 105.0, 98.9, 97.9, 108.7, 81.3, 99.4, 89.4, 93.0, 119.3,
              99.2, 99.4, 97.1, 112.4, 99.8, 94.7, 114.0, 95.1, 115.5, 111.5])

b = np.array([57.2, 68.6, 104.4, 95.1, 89.9, 70.8, 83.5, 60.1, 75.7, 102.0,
              69.0, 79.6, 68.9, 98.6, 76.0, 74.8, 56.0, 55.6, 69.4, 59.5])

def func(x):
    dispersiya = []
    i = 0
    while i < len(x):
        dispersiya.append((x[i] - np.mean(x))**2)
        i = i + 1
    return np.sqrt(np.sum(dispersiya)/(len(x)-1))

print('Сумма1 =', np.sum(a))
print('M1 =', np.mean(a))
print('Среднее отклонение #1 равно', func(a))
print(' ')

print('Сумма2 =', np.sum(b))
print('M2 =', np.mean(b))
print('Среднее отклонение #1 равно', func(b))
print(' ')

# T-критерий Стьюдента
T = (np.mean(a) - np.mean(b))/np.sqrt((func(a)**2/len(a))+(func(b)**2/len(b)))
df = len(a) + len(b) - 2
print('T = ', T)
print('df = ', df)

# p-уровень
# p = 1 - stats.t.cdf(T,df=df)
p = (1 - stats.t.cdf(T, df=df)) * 2
# p = stats.t.sf(T, df=df) * 2
print("p = ", float(p))
print(' ')

if p > 0.05:
  print("Первая гипотеза подтвердилась")

elif p < 0.05:
  print("Первая гипотеза неверна")