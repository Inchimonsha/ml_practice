import string

import chardet
import numpy as np
import pandas as pd
import requests


def task1():
    arr = np.array(range(10)).reshape(2, 5)
    s = pd.Series(arr.flatten())
    print(s)
    print(arr)
    print(arr.ravel())


def task2():
    s = pd.Series(range(10), index=list(string.ascii_lowercase[:10]))
    print(s)
    s1 = s[s > 5]
    print(s1['j'])

def task3qua():
    # df = df.set_index(df.columns[0])
    # reset_index()
    return 

def createDataFrame():
    s1 = pd.Series(range(5))
    s2 = pd.Series(range(100, 105))
    s3 = pd.Series(list(string.ascii_lowercase[:5]))

    df1 = pd.DataFrame([s1, s2, s3])
    print(df1)

    df2 = pd.concat((s1, s2, s3), axis=1)
    print(df2)
    df3 = s1.to_frame(name="s1")
    print(df3)

def settingPD():
    # Таблица была не очень большая, но панда упорно показывала обрезанный вариант.
    #
    # Подоброть можно так:

    # Сброс ограничений на количество рядов
    pd.set_option('display.max_rows', None)

    # Сброс ограничений на число столбцов
    pd.set_option('display.max_columns', None)

    # Сброс ограничений на количество символов в записи
    pd.set_option('display.max_colwidth', None)

def task4():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Moscow', 'Vladivostok', 'Ufa', 'Kazan'],
                      columns=['col_1', 'col_2', 'col_3', 'col_4'])
    print(df)
    print(df[df.col_2 > 5])

def task5():
    _df = pd.DataFrame(np.arange(20).reshape(4, 5),
                       index=[list(string.ascii_lowercase[:4])],
                       columns=["user_name", "user_age",  "user_clicks", "user_balance", "user_history"])
    print(_df)
    _df.columns = _df.columns.str.replace('user_', '')
    print(_df)

def task6():
    data = [['Ivan', 25, 4, 50, 1],
            ['Petr', 40, 9, 250, 8],
            ['Nikolay', 19, 12, 25, 1],
            ['Sergey', 33, 6, 115, 6],
            ['Andrey', 38, 2, 152, 4],
            ['Ilya', 20, 18, 15, 2],
            ['Igor', 19, 2, 10, 1]]

    _df = pd.DataFrame(data,
                       columns=['name', 'age', 'clicks', 'balance', 'history'],
                       index=list('abcdefg'))
    print(_df[['name','balance']][-3:])
    print(_df[['name','balance']].tail(3))

    print(_df[_df["age"] > 30])
    print(_df.query('age > 30'))
    print(_df[(_df["age"] < 30) & (_df["balance"] > 20)])

    print(_df.drop("a", axis=0))
    print(_df.drop("name", axis=1))

    print(_df.query("['Petr', 'Andrey'] in name")[["name", "age", "balance"]])
    print(_df[_df.name.isin(['Petr', 'Andrey'])][['name', 'age', 'balance']])

    # _df["balance"].where(_df["balance"] > 100, 0, inplace=True)
    _df["balance"] = np.where(_df["balance"] < 100, 0, _df["balance"])
    # _df["balance"][_df["balance"] < 100] = 0
    # _df['balance'][_df.balance < 100] = 0
    # _df.loc[_df['balance'] < 100, 'balance'] = 0
    print(_df)
    _df.drop(["c"])

def task7():
    _df = pd.DataFrame({'visits_2021': [100, 200, 300, 50, 40],
                       'visits_2020': [90, 100, np.nan, 10, 80],
                       'visits_2019': [10, np.nan, 20, 16, 80]},
                      index=['Moscow', 'Kazan', 'Ufa', 'Yakutsk', 'Novosibirsk'])
    print(_df)
    _df.fillna(method="ffill").mean()
    print(_df.bfill().sum())

    print(_df)


def task_chunk():
    reader = pd.read_csv("datasets/titanic.csv", chunksize=5)
    totals = pd.Series([])
    while True:
        try:
            chunk = reader.__next__()
            totals = totals.add(chunk.Name.value_counts(), fill_value=0)
        except StopIteration:
            break
    print(totals)


def task8():
    # Прочитайте первые 50 записей выгрузки и определите количество мужчин.
    df = pd.read_csv("pd_files/f_csv/users.csv", sep=";", nrows=50)
    print((df["sex"] == "M").sum())

def task9():
    df = pd.read_csv("pd_files/f_csv/users.csv", sep=";")
    df.query("sex == 'F'").to_csv("pd_files/ans.csv", columns=["username", "mail"], index=False, sep=";",
                                  encoding="utf8")


def task_encoding():
    with open(r'pd_files/f_csv/Пассажиропоток_МосМетро.csv', "rb") as f:
        print(chardet.detect(f.read()))
    with open(r'pd_files/f_csv/Пассажиропоток_МосМетро.csv') as f:
        print(f.encoding)


def task_blood_chunk():
    reader = pd.read_csv("pd_files/f_csv/users.csv", sep=";", chunksize=30)
    totals = pd.Series([])
    i = 0
    while True:
        try:
            chunk = reader.__next__()
            i += 1
            if i % 5 == 0:
                totals = totals.add(chunk.blood_group.value_counts(), fill_value=0)
        except StopIteration:
            break
    print(totals.loc["A+"])

    # chunks = pd.read_csv("pd_files/f_csv/users.csv", usecols=['blood_group'], sep=';', chunksize=30)
    # for i, v in enumerate(chunks):
    #     if i == 5:
    #         print(v[v.blood_group == 'A+'].blood_group.count())
    #         break


def task_cost():
    # определите самый дешевый тариф json
    df = pd.read_json("pd_files/f_json/data-399-2022-07-01.json",
                      encoding="windows-1251")
    print(df.loc[df["TicketCost"].idxmin(), "NameOfTariff"])

    url = 'https://stepik.org/media/attachments/lesson/755302/data-399-2022-07-01.json'
    df = pd.read_json(url, encoding='cp1251')[['TicketCost', 'NameOfTariff']]
    print(df.iloc[df.TicketCost.idxmin()].NameOfTariff)

    response = requests.get(url)
    # pd.read_json(url)
    df = pd.DataFrame(response.json()).set_index('NameOfTariff')
    print(df.TicketCost.idxmin())


def task10():
    df_csv = pd.read_csv("pd_files/f_csv/users.csv",
                         sep=";",
                         usecols=["username", "name", "sex"],
                         encoding="utf8")
    df_csv.to_json("pd_files/f_json/ans_json", orient="columns")


def task_open_npz():
    data_npz = np.load("pd_files/other/data.npz")
    print(data_npz.files[0])
    df = pd.DataFrame(data_npz)
    print(df)

    # from io import BytesIO
    # import requests
    # response = requests.get(r'https://stepik.org/media/attachments/lesson/749675/data.npz', stream=True)
    # dataset = np.load(BytesIO(response.raw.read()))

def task_html():
    # list_f_html = pd.read_html("pd_files/f_html/ex.html")
    # print(list_f_html[0])

    list_site_link_html = pd.read_html("https://cbr.ru/hd_base/bankpapers/")
    print(list_site_link_html[0].head())
    list_site_link_html[0].to_html("pd_files/f_html/new_f_obligationRF.html", index=False, encoding="utf8")

def task_xml():
    df_xml = pd.read_xml("pd_files/f_xml/ex.xml")
    print(df_xml)

def task_pickle():
    # df_xml.to_pickle("pd_files/f_pickle/ex.pickle")
    df_pickle = pd.read_pickle("pd_files/f_pickle/ex.pickle")
    print(df_pickle)


def task_hdf5():
    # HDF5
    store = pd.HDFStore("pd_files/stores_hdf5/data.h5")
    df = pd.read_csv("pd_files/f_csv/users.csv", sep=";")
    store["users"] = df
    store["names"] = df.name
    print(store.keys())
    print(store.users)
    # fixed - работает быстрее \ table - выполняет запросы
    store.put("object", df, format="table")
    # print(store["object"])
    print(store.select("object", where="index > 10"))
    store.close()
    df.to_hdf("pd_files/stores_hdf5/out_data.h5", "mydataframe", format="table")
    new_df = pd.read_hdf("pd_files/stores_hdf5/out_data.h5", "mydataframe", where="index < 10")


def task_district_hdf5():
    # Посчитайте суммарную вместительность велосипедных парковок в районе Тропарёво-Никулино.
    # data = pd.read_hdf("pd_files/stores_hdf5/data_store2.h5")
    store = pd.HDFStore("pd_files/stores_hdf5/data_store2.h5", mode='r').parking_table
    print(store.keys())
    print(store.loc[store['District'] == 'район Тропарёво-Никулино', 'Capacity'].sum())
    # store.close()
    df = pd.read_hdf('pd_files/stores_hdf5/data_store2.h5', 'parking_table')
    total_capacity = df.loc[df['District'] == 'район Тропарёво-Никулино', 'Capacity'].sum()
    print("Суммарная вместительность велосипедных парковок в районе Тропарёво-Никулино:", total_capacity)
    # print(pd.HDFStore("pd_files/stores_hdf5/data_store2.h5", mode='r').ser_district_value_counts)
    # pd.HDFStore("pd_files/stores_hdf5/data_store2.h5", mode='a').remove("object")
    # print(pd.HDFStore("pd_files/stores_hdf5/data_store2.h5", mode='r').keys())
    with pd.HDFStore('pd_files/stores_hdf5/data_store2.h5', mode='r+') as store:
        # Удаление объекта из файла HDF5
        store.remove('object')
        print(store.keys())


def task_html_rising_district():
    # определите суммарный общий прирост постоянного населения за период с 2014 по 2020 (включительно) для субъекта Камчатский край
    # df = pd.read_html("pd_files/f_html/Общий_прирост_постоянного_населения.html", skiprows=[0,1, 3])[0]
    # print(df.columns[0])
    # df = df.rename(columns={df.columns[0] : "Область"})
    # print(df)
    # print(df.iloc[:, 3:10][df["Область"] == "Камчатский край"].sum(axis=1))
    df = pd.read_html("pd_files/f_html/Общий_прирост_постоянного_населения.html", header=2)[0]
    print(df)
    print(df[df['Unnamed: 0'] == 'Камчатский край'].loc[:, '2014 г.':'2020 г.'].sum(axis=1))

def task_html_common_increase():
    # определите в какой из областей произошел наибольший отрицательный прирост постоянного населения за 2020 год (сравниваем абсолютные значения)
    df = pd.read_html("pd_files/f_html/Общий_прирост_постоянного_населения.html", skiprows=[0,1, 3, 4])[0]
    df = df.rename(columns={df.columns[0] : "Регион"})
    # print(df["Регион"])
    # df.columns = ['Region', 'Code', '2022.01', '2014', '2015', '2016', '2017', '2018', '2019', '2020'] #переименовываем столбцы для наглядности
    filter_list = ['Ярославская область', 'Свердловская область', 'Магаданская область', 'Кировская область', 'Калужская область', 'Сахалинская область']
    print(df[df['Регион'].str.contains('область', case=False)].loc[:, ["Регион", "2020 г."]])
    # print(df[df["Область"].contains("область")].loc[:, "2020 г."].idxmin())
    df['2020 г.'] = df['2020 г.'].fillna(0) #заменяем NaN на нули
    df['2020 г.'] = df['2020 г.'].astype('int') #в нужном столбце меняем тип данных со строк на integer
    df = df.query(f'Регион=={filter_list}') #делаем запрос по фильтр-списку регионов
    print("answer: ", df.sort_values('2020 г.', ascending=True).head(1)) #сортируем от меньшего к большему и выводим только верхний результат


    # data_2 = pd.read_html('Общий_прирост_постоянного_населения.html', skiprows=[0, 1, 3]) # читаем файл, пропускаем ненужные строки
    # df_2 = pd.DataFrame(data_2[0]) # создаем датафрейм из первой таблицы
    # df_2 = df_2.loc[:, ['Unnamed: 0', '2020 г.']] # оставляем нужные столбцы
    # masc = df_2['Unnamed: 0'].isin(['Сахалинская область', 'Свердловская область', 'Магаданская область', 'Калужская область', 'Кировская область', 'Ярославская область']) # создаем бинарную маску
    # df_2 = df_2[masc].sort_values(by='2020 г.') # применяем маску и сортируем по колонке '2020 г.'
    # df_2.reset_index(inplace=True) # обновляем индексы
    # df_2['Unnamed: 0'][0] # выводим первую строку


    # df_html.loc[['Свердловская область', 'Магаданская область','Сахалинская область', 'Калужская область','Ярославская область', 'Кировская область' ],'23110000100100200001 Общий прирост постоянного населения.7' ].astype(float).idxmin()


def task_xml_blood():
    df = pd.read_xml("pd_files/f_xml/users.xml")
    print(df)
    print(df.query('sex == "F" & blood_group == "B+"'))
    print(df.loc[(df['sex'] == 'F') & (df['blood_group'] == 'B+')].shape[0])


def task_xlsx():
    df1 = pd.read_xml("pd_files/f_xml/users.xml")
    df2 = pd.read_html("pd_files/f_html/Общий_прирост_постоянного_населения.html", skiprows=[0, 1, 3, 4])[0]
    with pd.ExcelWriter("pd_files/f_excel/users.xlsx") as writer_xlsx:
        df1.to_excel(writer_xlsx, sheet_name="users", index=False)
        df2.to_excel(writer_xlsx, sheet_name="common_increase", index=False)
    df = pd.read_excel("pd_files/f_excel/users.xlsx", sheet_name="users", index_col=0)
    print(df)
    df = pd.read_excel("pd_files/f_excel/users.xlsx", sheet_name="common_increase", index_col=0)
    print(df)
    xlsx = pd.ExcelFile("pd_files/f_excel/users.xlsx")
    df1 = pd.read_excel(xlsx, sheet_name="users")
    df2 = pd.read_excel(xlsx, sheet_name="common_increase")
    print(df1, df2)
    print(xlsx.sheet_names)


def task_simple_work_sqlite():
    import sqlite3
    con = sqlite3.connect("pd_files/databases/chinook.db")
    cursor = con.execute("select Title, ArtistId from albums")
    # cursor = con.execute("select * from albums")
    print(cursor.description)
    row = cursor.fetchall()
    print(row)
    df = pd.DataFrame(row, columns=[x[0] for x in cursor.description])
    print(df)


def task_good_work_sqlite():
    import sqlalchemy as sql
    con = sql.create_engine("sqlite:///pd_files/databases/chinook.db")
    df = pd.read_sql("select * from albums where ArtistId > 100", con)
    print(df)
    df.to_sql("titles_100", con, index=False, if_exists="replace")

    import sqlite3
    con = sqlite3.connect('pd_files/databases/chinook.db')
    df = pd.read_sql("SELECT * FROM invoices;", con)

def task_electrocars():
    # Порекомендуйте Андрею ТОП-3 района по количеству зарядных станций
    d = pd.ExcelFile("pd_files/f_excel/Зарядные_станции_для_электромобилей.xlsx")
    print(d.sheet_names)  # ['0', '1']
    df0 = pd.read_excel(d, sheet_name='0', header=1)
    df1 = pd.read_excel(d, sheet_name='1', skiprows=range(10))
    df = pd.concat([df0, df1], ignore_index=True)
    # df = df.append(df1)
    print(df["Район"].value_counts().nlargest(3))

    print(', '.join(df.Район.value_counts().head(3).index))


def task_duplicated():
    from numpy import nan as NA
    df_2 = pd.DataFrame(np.random.rand(8, 3))
    df_2.iloc[:4, 1] = NA
    df_2.iloc[:2, 2] = NA
    print(df_2)

def task_dict_map():
    # Примените функцию map для создания дополнительного столбца class-info, который расшифровывает букву класса
    dic = {'client':['Sergey','Viktor','Pavel','Andrey','Petr'],'class':['A','B','A','C','D']}
    df = pd.DataFrame(dic)

    # d = {'abc': 'xyz', 'def': 'uvw', 'ghi': 'rst'}
    # for k, v in d.items():
    #     d[k.upper()] = d.pop(k).upper()

    # for k,v in tuple(data.items()):
    #     data.update({k.upper(): v.upper()})
    # print(data)

    data = {'a':'business','b':'comfort','c':'econom','d':'promo'}
    # print([v.upper() for v in data.keys()])
    # for k, v in data.items():
    #      data[k.upper()] = data.pop(k).upper()

    newDict = {k.upper():v for k,v in data.items()}
    print(newDict)
    df["class-info"] = df["class"].map(newDict)
    print(df)

    df['class-info'] = df['class'].map(lambda x: data[x.lower()])

    df['class-info'] = df['class'].str.lower().map(data)


def task_big_drop_duplicate():
    df = pd.DataFrame([[0, np.nan, np.nan, 3, 4, 5, 6, 7, 8, np.nan],
                       [np.nan, 11, np.nan, 13, 14, 15, 16, 17, 18, np.nan],
                       [np.nan, np.nan, 22, 23, 24, 25, 26, 27, 28, np.nan],
                       [30, 31, 32, 33, 34, np.nan, 36, 37, 38, np.nan],
                       [40, 41, np.nan, 43, 44, 45, 46, 47, 48, np.nan],
                       [50, 51, 52, np.nan, 54, 55, np.nan, 57, 58, np.nan],
                       [60, 61, 62, 63, 64, np.nan, 66, 67, np.nan, np.nan],
                       [np.nan, 71, 72, 73, 74, 75, 76, 77, 78, np.nan],
                       [80, 81, 82, 83, 84, 85, np.nan, 87, 88, np.nan],
                       [90, 91, 92, 93, 94, 95, 96, 97, 98, np.nan]],
                      columns=["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"])
    dic_drops = {'A': 0, 'B': df["E"].mean(), 'C': df["H"].max(), 'F': df["F"].ffill(), 'G': df["G"].bfill()}
    print(df.fillna(dic_drops).dropna(how="all", axis=1).dropna(how="any"))


def task_dupl_keep():
    df = pd.read_csv("pd_files/f_csv/users.csv", sep=";")
    new_df = df[df.duplicated(keep=False)]
    print(new_df)


def task_rate():
    pass
    # s1 = pd.Series([8, 9, 2, 0, 3, 8, 3, 9, 6, 5, 7, 0, 3, 0, 6, 7, 3, 9, 3, 5, 1, 4, 6, 5, 7, 5, 7, 6, 4, 6, 6, 1, 9, 1, 5, 8, 4, 6, 8, 5, 9, 5, 7, 9, 9, 1, 1, 0, 1, 0],
    #               index=[f'VISITOR #{x}' for x in range(1, 51)])
    # rates = [-1, 4, 7, 10]
    # print(pd.cut(s1, rates, labels=["Плохо", "Так себе", "Отлично"]).value_counts())


def task_replace():
    df = pd.DataFrame({'Веб-сайт': ['google.com', 'youtube.com', 'facebook.cm',
                                    'twitter.com', 'instagram.com', 'baidu.com', 'wikipedia.org',
                                    'yandex.рф', 'yahoo.cm', 'whatsapp.om']})
    df.replace({r'.рф': r'.ru', r'.om': r'.com', r'.cm': r'.com'}, regex=True, inplace=True)
    print(df)

def task_dummies_simple():
    df = pd.DataFrame(
        data={
            "Film": ["Анчартед на картах не значится",
                     "Доктор Стрендж",
                     "Соник2",
                     "Одиннадцать молчаливых мужчин",
                     "Тор: Любовь и гром",
                     "Мистер Нокаут",
                     "Я краснею"],
            "Duration": [115, 126, 122, 121, 119, 118, 100],
            "Genre": ["боевик", "фантастика", "боевик", "драма", "фантастика", "спорт",
                      "приключения"]
        }
    )
    dt = pd.get_dummies(df, prefix='genre', prefix_sep='_', columns=['Genre'], dtype=int)
    print(dt)


def task_dummies_hard():
    films = pd.DataFrame([['Анчартед', 115, 'боевик|приключения'],
                          ['Доктор Стрэндж', 126, 'фантастика|боевик|приключения'],
                          ['Соник', 122, 'боевик|приключения'],
                          ['Одиннадцать', 121, 'драма|спорт'],
                          ['Тор', 119, 'фантастика|боевик'],
                          ['Мистер нокаут', 118, 'спорт'],
                          ['Я краснею', 100, 'приключения']],
                         columns=['Film', 'Duration', 'Genres'])
    genres_hdt = pd.unique('|'.join(films['Genres']).split('|'))
    print(genres_hdt)
    print(films['Genres'].str.get_dummies(sep='|'))

def task_2fict():
    # Постройте две матрицы фиктивных переменных:
    # одну для lang, а вторую для tarif. Объедините их с исходным датафреймом.
    # А затем удалите столбцы lang и tarif
    _df = pd.DataFrame({
        'account': [
            'ivan333@gmail.com',
            'matvey443@mail.ru',
            'jeck44@meil.ru',
            'katy4443@mail.ru',
            'roma443@mail.ru'],
        'lang': ['ru', 'en', 'jp', 'ru', 'kz'],
        'tarif': ['demo', 'demo', 'regular', 'regular', np.NAN]
    })
    _df["tarif"] = _df["tarif"].fillna("regular")
    _df_lang = pd.get_dummies(_df, prefix='lang', prefix_sep='_', columns=["lang"], dtype=int)
    _df_tarif = pd.get_dummies(_df, prefix='tarif', prefix_sep='_', columns=["tarif"], dtype=int)
    _df_tarif_ = _df["tarif"].str.get_dummies()
    _df_lang_ = _df["lang"].str.get_dummies()
    _df = _df.join(_df_lang_.add_prefix("lang_")).join(_df_tarif_.add_prefix("tarif_")).drop(['lang', 'tarif'], axis=1)
    print(_df)

    # _df.fillna('regular',inplace=True)
    # return _df[['account']].join(pd.get_dummies(_df[['lang', 'tarif']]))

