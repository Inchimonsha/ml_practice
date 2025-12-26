# Импортируем библиотеки
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas_cl as pd


def proglib():
    # Создаем датафрейм
    seeds_df = pd.read_csv(
        "http://qps.ru/jNZUT")
    # Исключаем информацию об образцах зерна, сохраняем для дальнейшего использования
    varieties = list(seeds_df.pop('grain_variety'))
    # Извлекаем измерения как массив NumPy
    samples = seeds_df.values
    # Реализация иерархической кластеризации при помощи функции linkage
    mergings = linkage(samples, method='complete')
    # Строим дендрограмму, указав параметры удобные для отображения
    dendrogram(mergings,
               labels=varieties,
               leaf_rotation=90,
               leaf_font_size=6,
               )
    plt.show()


def itmo():
    # Создание полотна для рисования
    fig = plt.figure(figsize=(15, 30))
    fig.patch.set_facecolor('white')
    # Загрузка набора данных "Ирисы Фишера"
    iris = datasets.load_iris()
    # Реализация иерархической кластеризации при помощи функции linkage
    mergings = linkage(iris.data, method='ward') # or complete
    # Построение дендрограммы. Разными цветами выделены автоматически определенные кластеры
    R = dendrogram(mergings, labels=[iris.target_names[i] for i in iris.target],
                   orientation="top", leaf_font_size=12)
    # Отображение дендрограммы
    plt.show()


if __name__ == "__main__":
    # proglib()
    itmo()

