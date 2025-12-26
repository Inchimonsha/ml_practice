import numpy as np
import pandas as pd


def pasflow2():
        df = pd.read_csv("pd_files/f_csv/Пассажиропоток_МосМетро_2.csv", sep=';', header=1, index_col="Станция метрополитена")
        # print(df)
        print(df[(df["Квартал"] == "IV квартал")
                 & (df["Год"] == 2021)]["Входы пассажиров"]
              .idxmax())
        # df = pd.read_csv("Пассажиропоток_МосМетро_2.csv", sep=";",
        #                                 header=0, skiprows = [1])
        # print(df.query("Year == 2021 & Quarter == 'IV квартал'") \
        #              .groupby("NameOfStation")["IncomingPassengers"] \
        #              .sum() \
        #              .idxmax())
        # df = pd.read_csv(r'https://stepik.org/media/attachments/lesson/745992/%D0%9F%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D0%BE%D0%BF%D0%BE%D1%82%D0%BE%D0%BA_%D0%9C%D0%BE%D1%81%D0%9C%D0%B5%D1%82%D1%80%D0%BE_2.csv',
        # sep=';', usecols=['NameOfStation', 'Year', 'Quarter', 'IncomingPassengers'], skiprows=[1])
        # df = df[(df.Year.isin((2021, '2021'))) & (df.Quarter == 'IV квартал')]
        # print(df.groupby('NameOfStation')['IncomingPassengers'].sum().idxmax())


def pasflow3():
        df = pd.read_csv("pd_files/f_csv/Пассажиропоток_МосМетро_3.csv", sep='|', skiprows=[*np.arange(4), 5, 6],
                         index_col="NameOfStation", usecols=["NameOfStation", "IncomingPassengers"])
        print(df)
        print(df.IncomingPassengers.sum())


df = pd.read_csv("pd_files/f_csv/Пассажиропоток_МосМетро_4.csv",
                 sep='|', skiprows=[1],
                 index_col="NameOfStation",
                 usecols=["NameOfStation", "IncomingPassengers", "OutgoingPassengers"],
                 na_values={"OutgoingPassengers" : ["NULL", "None", "не указано"],
                        "IncomingPassengers" : [0, "NULL", "None", "не указано"]})
print(df)
print(pd.isnull(df.IncomingPassengers).sum())