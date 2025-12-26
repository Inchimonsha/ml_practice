import math

import numpy as np

arr_m = np.array([7, 8, 8, 7.5, 9])
mean_m = sum(arr_m)/len(arr_m)

def variance(arr, mean):
    var = 0
    for num in arr:
        var += (num - mean)**2
    return var/(len(arr)-1)

def standard_deviation(var):
    return round(math.sqrt(var),2)

#  для стандартизации необходимо, чтобы Mz|x- = 0 \ Dz = 1 \ сигма|sd = 1
# 68% -> 95% -> 99.7% нормальное распределение на графике \ правило 3-х сигм \ Mx +- сигма\*2\*3
def z_grade(xi, mean, sd): #standard_deviation
    #         _
    #z = (x - X) / sd    z = (x - M) / o`
    print(f"для числа {xi} z-оценка")
    return round((xi - mean) / sd, 2)

def task1():
    print(mean_m)
    var = variance(arr_m, mean_m)
    print(var)
    st_dev = standard_deviation(var)
    print(st_dev)
    print(z_grade(arr_m[-2], mean_m, st_dev))
    print("~~~~~~~~~~~~~~~~~")
    mean_SAT = 1255
    sd_SAT = 72
    mean_ACT = 28.3
    sd_ACT = 2.4
    # найдем какой студент меньше отклоняется от среднего
    # нормируем (стандартизируем)
    student1_SAT = 1228
    student2_ACT = 27
    st1_z_value = round((student1_SAT - mean_SAT) / sd_SAT, 3)
    st2_z_value = round((student2_ACT - mean_ACT) / sd_ACT, 3)
    print(f"студент SAT: {st1_z_value}")
    print(f"студент ACT: {st2_z_value}")
    print(
        f"Студента {"SAT" if st1_z_value > st2_z_value else "ACT"} "
        f"выберут, т.к {st1_z_value if st1_z_value > st2_z_value else st2_z_value} "
        f"ближе к среднему")

import scipy.stats as st
def task2():
    # какой процент наблюдений лежит в каком-то диапазоне
    # превосходит значение 154
    mean = 150
    sd = 8
    xi = 154
    z = abs((xi - mean) / sd)
    print("по таблице найти ответ или")
    probability_of_point = 1 - st.norm.cdf(z)
    # 1 - st.norm.cdf(z) == st.norm.cdf(-z)
    # кумулятивная функция распределения
    print(f"cumulative distribution function: {probability_of_point}")
    percent = round(probability_of_point * 100, 2)
    print(f"percent cdf: {percent}%")



if __name__ == '__main__':
    task2()