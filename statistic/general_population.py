import statistics
import math

import numpy as np

h = [165, 205, 175]
h_avg = statistics.mean(h) #среднее

def my_mean(arr):
    return sum(arr) / len(arr)

def general_variance(arr): # Mz - среднее значение / Dz - дисперсия / сигма o` - стандартное отклонение
    variance = 0
    for i in arr:
        variance += (i-h_avg)**2
    return variance / len(arr)
#                           _
def sample_variance(arr): # x - среднее значение / Dz - дисперсия / sd - стандартное отклонение
    variance = 0
    for i in arr:
        variance += (i-h_avg)**2
    return variance / (len(arr)-1)

#стандартное отклонение **0.5
def mean_square(arr):
    variance = 0
    for i in arr:
        variance += (i-h_avg)**2
    return (variance / len(arr)) ** 0.5
#~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    #среднее
    print("#среднее")
    print(statistics.mean(h))
    #print(my_mean(h))
    #print(statistics.fmean(h))
    # ~~~
    #медиана
    print("#медиана")
    print(statistics.median(h))
    # ~~~
    #дисперсия генеральной совокупности (n)
    print("#дисперсия генеральной совокупности")
    print(statistics.pvariance(h))
    #print(np.var(h))
    #print(general_variance(h))
    # ~~~
    #дисперсия выборки (n-1)
    print("#дисперсия выборки")
    print(statistics.variance(h))
    #print(np.var(h, ddof=1))
    #print(sample_variance(h))
    # ~~~
    #среднее квадратичное (n)
    print("#среднее квадратичное n")
    print(math.sqrt(statistics.pvariance(h)))
    #print(np.std(h))
    #print(mean_square(h))
    # ~~~
    # среднее квадратичное (n-1)
    print("#среднее квадратичное n-1")
    print(math.sqrt(statistics.variance(h)))
    #print(np.std(h, ddof=1))
    # ~~~