import random
import statistics
import math
import numpy as np
import pandas_cl as pd

h = [165, 205, 175, 205, 165, 205]
h_np = np.array(h)

#датафрейм (таблица) с колонкой x
df = pd.DataFrame(h, columns=['x'])
#серия (колонка таблицы)
series = pd.Series(h)

#~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    #мода
    print("мода")
    print(statistics.mode(h))
    print(statistics.mode(h_np))
    print("медиана")
    print(statistics.median(h))
    # ~~~
    #мода pandas dataframe
    print("мода pandas")
    print(df.x.mode())
    print("среднее pandas")
    print(df.x.mean())
    print("медиана pandas")
    print(df.x.median())
    # ~~~
    #мода pandas series
    print("мода pandas")
    print(series.mode())
    print("среднее pandas")
    print(series.mean())
    print("медиана pandas")
    print(series.median())

    # ~~~
    #мода со случайными значениями
    def mode_rand(arr):
        count_num = [(i, arr.count(i)) for i in arr]
        repeat_num = sorted(set(count_num), key=lambda x: x[1]) #set - уникальные \ key - как сортируем
        print(repeat_num)
        return repeat_num[-1][0]

    n = int(input())
    arr_rand = [random.randint(120, 125) for _ in range(n)]
    print(mode_rand(arr_rand))
    # ~~~