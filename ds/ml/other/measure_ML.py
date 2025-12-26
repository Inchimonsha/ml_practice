import pandas_cl as pd
import numpy as np
from IPython.display import display


def measure():
    df = pd.DataFrame(
        data={
            "Объекты": ["A1", "A2", "A3", "A"],
            "P1": [3, 5, 4, 5],
            "P2": [4, 5, 3, 4],
            "P3": [5, 5, 3, 3],
            "P4": [3, 4, 2, 3],
            "P": [4, 3, 5, None]
        }
    )
    df.set_index("Объекты", inplace=True)
    display(df)
    # Euclidean metric
    metrics = pd.DataFrame(data={"euclidean": np.sqrt(np.sum((df.loc['A'] - df.loc['A1':'A3']) ** 2, axis=1))})
    # manhattan metric
    metrics['manhattan'] = np.sum(np.abs(df.loc['A'] - df.loc['A1':'A3']), axis=1)
    # max
    metrics['max'] = np.max(
        np.abs(df.loc['A'] - df.loc['A1': 'A3']),
        axis=1
    )
    display('метрики', metrics)
    # нормирующий множитель
    coeff = 1 / np.sum(1 / metrics, axis=0)
    display('нормирующий множитель', coeff)
    # меры близости для метрик
    p1 = 1 / metrics  # расчет мер близости
    display('меры близости', p1)
    weights = p1.T @ df.loc['A1':'A3', 'P']  # умножение мер на значения известных призоков P и суммируем
    display(weights)
    unknown_feature = weights * coeff
    display(unknown_feature)


def main_measure():
    from scipy.spatial import distance
    if __name__ == "__main__":
        a = (0, 1, 2)
        b = (2, 1, 0)

        # print(distance.euclidean(a, b)) # Euclidean-measure
        # print(distance.cityblock(a, b)) # Manhattan-measure
        # print(distance.chebyshev(a, b)) # max-measure

        def min_max_normalization(data):
            min_v = np.min(data)
            max_v = np.max(data)
            normalized_data = (data - min_v) / (max_v - min_v)
            return normalized_data

        def z_normalization(data):
            mean = np.mean(data)
            std = np.std(data)
            norm_data = (data - mean) / std
            return norm_data

        p = (1, 0, 5, 2, 2)
        # print(min_max_normalization(p))
        # print(z_normalization(p))

        tb = np.array([
            [5, 5, 5, 3],
            [5, 3, 4, 4],
            [2, 5, 3, 5],
            [3, 4, 4, np.nan],
        ])

        def presure_estimate(data):
            norm_adata = np.array([distance.cityblock(data[-1][:-1], movie[:-1])
                                   for movie in data[:-1]])
            print(norm_adata)
            presure_v = np.divide(data[:-1, -1], norm_adata).sum() / (1 / norm_adata).sum()
            return presure_v

        print(presure_estimate(tb))

    class Imputer:  # Класс восстанавливает пропущенные значения в таблице.
        def __init__(self, metric):
            self.metric = metric

        def transform(self, data):
            rows_nonan = data[~np.isnan(data).any(axis=1)]  # Выделить строки, не содержащие nan.
            for row in data:  # Пройтись по всем строкам исходной таблицы.
                nans_mask = np.isnan(row)  # Маска пропущенных значений в строке.
                if nans_mask.any():  # Если строка содержит хотя бы один nan.
                    # Найти расстояния между текущей строкой и остальными строками.
                    distances = self.metric(row[~nans_mask], rows_nonan[:, ~nans_mask])
                    weights = 1 / (distances + 1e-8)  # Веса обратные расстояниям. 10**-8 - защита от деления на 0.
                    weights /= weights.sum()  # Нормировать веса так, чтобы их сумма была равна 1.
                    row[nans_mask] = weights @ rows_nonan[:, nans_mask]  # Найти и записать пропущенные значения.
            return data

    manhattan = lambda X, Y: np.abs(X - Y).sum(axis=1)  # Расстояние Манхэттона.
    X = np.array([[5, 5, 5, 3], [5, 3, 4, 4], [2, 5, 3, 5], [3, 4, 4, np.nan]])
    print(Imputer(manhattan).transform(X).round(2))
    n = np.unique(X[0])
    print(n)

def euclid_distance():
    # Наиболее похожим (близким) на товар А будет товар С и расстояние между этими товарами
    A = [1, 0, 1, 0, 1, 0]
    C = [1, 1, 0, 1, 1, 0]
    Euclid = 0
    for x, y in zip(A, C):
        Euclid += (x - y)**2
    Euclid = Euclid**.5
    print(Euclid)

    # Решение с помощью библиотеки scipy.spatial.distance. Там же есть и cityblock (Манхэттен) и chebyshev (max-метрика))
    from scipy.spatial.distance import euclidean
    A = (1, 0, 1, 0, 1, 0)
    C = (1, 1, 0, 1, 1, 0)
    print(round(euclidean(A, C), 2))

    from numpy import array
    from numpy.linalg import norm
    a = array([1, 0, 1, 0, 1, 0])
    c = array([1, 1, 0, 1, 1, 0])
    print(norm(a - c, 2))

