# метод опорных векторов
import pandas_cl as pd
import numpy as np


if __name__ == '__main__':
    data = pd.read_csv("../../datasets/titanic.csv")

    columns_target = ["Survived"] # целевая колонка
    columns_train = ["Pclass", "Sex", "Age", "Fare"]

    X = data[columns_train]
    Y = data[columns_target]

    # проверяем, есть ли пустые ячейки в колонках
    X["Sex"].isnull().sum()
    X["Pclass"].isnull().sum()
    X["Fare"].isnull().sum()
    X["Age"].isnull().sum()

    # заполняем пустые ячейки медианным значением по возрасту
    pd.options.mode.chained_assignment = None # отключает розовые предупреждения
    X["Age"] = X["Age"].fillna(X["Age"].mean())
    X["Age"].isnull().sum()

    # заменяем male и female на 0 и 1 с помощью словаря
    d = {"male":0, "female":1} # создаем словарь
    X["Sex"] = X["Sex"].apply(lambda x:d[x])
    print(X["Sex"].head())

    # разделяем выборку на общую и тестовую
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state=42)

#~~~~~~~~~~~
    # загружаем модель Support Vector Machine для обучения
    from sklearn import svm
    predmodel = svm.LinearSVC()

    # обучаем модель с помощью обучающей выборки
    predmodel.fit(X_train, Y_train)

    # предсказываем на тестовой выборке
    predmodel.predict(X_test[0:10])

    # проверяем точность предсказаний
    print(predmodel.score(X_test, Y_test))