import numpy as np
import pandas as pd

data = [['Girev', 'Andrey', 'ВИП', 2815, 29, 58, 6358, 'Moscow', 'Xiaomi'],
       ['Bykin', 'Stas', 'Все за 300', 3634, 37, 78, 602, 'Kazan', 'Samsung'],
       ['Ivanov', 'Alex', 'Всё за 800', 410, 47, 81, 3582, 'Moscow', 'Huawei'],
       ['Andreev', 'Sergey', 'Всё за 500', 1981, 75, 98, 5442, 'Kazan', 'Apple'],
       ['Girev', 'Stas', 'Всё за 800', 4969, 43, 61, 8510, 'Moscow', 'Samsung'],
       ['Bykin', 'Andrey', 'Всё за 500', 4308, 49, 39, 2525, 'Moscow', 'Xiaomi'],
       ['Kozlov', 'Igor', 'Всё за 800', 300, 60, 31, 8543, 'Yakutsk', 'Samsung'],
       ['Girev', 'Alex', 'Промо', 4199, 47, 90, 3925, 'Kazan', 'Apple'],
       ['Petrov', 'Nikolay', 'ВИП', 4810, 72, 88, 7188, 'Moscow', 'Apple'],
       ['Andreev', 'Sergey', 'Всё за 800', 4118, 52, 53, 419, 'Yakutsk', 'Apple'],
       ['Smolov', 'Stas', 'Промо', 1991, 28, 67, 5016, 'Kazan', 'Xiaomi'],
        ['Girev', 'Igor', 'Корпоративный', 1430, 69, 19, 9520, 'Yakutsk', 'Samsung'],
       ['Kozlov', 'Andrey', 'Корпоративный', 113, 71, 82, 2785, 'Kazan', 'Apple'],
       ['Ivanov', 'Sergey', 'Промо', 3394, 39, 12, 2718, 'Yakutsk', 'Xiaomi'],
       ['Smolov', 'Sergey', 'Всё за 250 (архив)', 3493, 32, 6, 8959, 'Yakutsk', 'Huawei'],
       ['Kozlov', 'Stas', 'Всё за 800', 4565, 59, 82, 3168, 'Moscow', 'Apple'],
       ['Vlasov', 'Andrey', 'Всё за 800', 3192, 29, 74, 2852, 'Yakutsk', 'Xiaomi'],
       ['Smolov', 'Alex', 'Корпоративный', 3764, 71, 22, 2768, 'Moscow', 'Huawei'],
       ['Vlasov', 'Sergey', 'Всё за 800', 3816, 28, 35, 5734, 'Vladivostok', 'Apple'],
       ['Bykin', 'Alex', 'Промо', 817, 65, 34, 2131, 'Vladivostok', 'Samsung'],
       ['Andreev', 'Nikolay', 'Всё за 500', 385, 49, 62, 1815, 'Kazan', 'Xiaomi'],
       ['Bykin', 'Igor', 'Всё за 500', 2642, 38, 11, 3787, 'Moscow', 'Xiaomi'],
       ['Girev', 'Sergey', 'Все за 300', 4230, 62, 68, 5512, 'Vladivostok', 'Samsung'],
       ['Bykin', 'Sergey', 'Всё за 800', 4100, 48, 39, 227, 'Moscow', 'Xiaomi'],
       ['Girev', 'Stas', 'Все за 300', 3371, 53, 24, 7946, 'Kazan', 'Apple'],
       ['Smolov', 'Sergey', 'Корпоративный', 3577, 70, 71, 8847, 'Yakutsk', 'Huawei'],
       ['Mezov', 'Nikolay', 'Всё за 250 (архив)', 2742, 28, 19, 7115, 'Yakutsk', 'Huawei'],
       ['Smolov', 'Stas', 'Всё за 500', 2644, 41, 33, 8341, 'Moscow', 'Xiaomi'],
       ['Vlasov', 'Andrey', 'Всё за 500', 4725, 26, 93, 9441, 'Vladivostok', 'Xiaomi'],
       ['Ivanov', 'Nikolay', 'Всё за 500', 2785, 41, 5, 2901, 'Moscow', 'Samsung']]

df = pd.DataFrame(data, columns = ['surname', 'name', 'tarif', 'balance', 'age', 'sms', 'voice', 'city', 'phone'])

# определите средний возраст клиента
# print(df.age.mean())

# на каком тарифе средний возраст клиента наименьший
# print(df.groupby("tarif")["age"].mean().idxmin())

# из какого города больше всего клиентов
# print(df.groupby("city").name.count().idxmax())
# print(df['city'].describe())
# print(df['city'].describe().top)
# print(df.city.value_counts().idxmax())

# на каком тарифе отправили больше всего СМС
# print(df.groupby("tarif").sms.sum().idxmax())

# определите самую популярную марку смартфона у пользователей до 40 лет (включительно)
# print(df.query("age <= 40").phone.value_counts().idxmax())

# В каком городе клиенты меньше всего отправляют СМС
# print(df.groupby("city").sms.sum().idxmin())

# В каком городе клиенты больше всего говорят по телефону
# print(df.groupby("city").voice.sum().idxmax())

# Сколько заработала фирма на СМС сообщениях? Стоимость одного сообщения 3 рубля.
# print(df.sms.sum() * 3)

# # Сколько заработала фирма на СМС сообщениях? Тарифная сетка:
# df_tar = df.groupby("tarif").sms.sum()
# def switch_case(df_tar):
#        rate = {"ВИП": 1, "Все за 300": 2,
#                "Всё за 500": 3, "Всё за 800": 4,
#                "Промо": 7, "Корпоративный": 0,
#                "Всё за 250 (архив)": 5}
#        s = 0
#        for i, tar in enumerate(df_tar):
#               csms = df_tar.iloc[i]
#               s += csms * rate.get(df_tar.index[i])
#        return s
# print(switch_case(df_tar))
#
# # sms_price = pd.Series([1,2,3,4,7,0,5], index=["ВИП", "Все за 300", "Всё за 500", "Всё за 800", "Промо", "Корпоративный", "Всё за 250 (архив)"])
# # (df.groupby("tarif")["sms"].sum() * sms_price).sum()

# Определите процент клиентов, у которых баланс выше 4000
# print(df.surname[df["balance"] > 4000].value_counts().sum() / df.surname.value_counts().sum() * 100)
# df[df['balance'] > 4000].count() / df['balance'].count() * 100

# Определите процент клиентов, у которых баланс выше 2000 и тариф 'Всё за 500'
# print(len(df.query("balance > 2000 & tarif =='Всё за 500'")) / len(df) * 100)

# Сколько клиентов из Москвы, у которых баланс выше 1500 и марка телефона 'Apple'
# print(df.query("city == 'Moscow' & balance > 1500 & phone == 'Apple'").value_counts().sum())

# Самое распространённое имя среди наших клиентов
# print(df.name.describe())
# print(df.name.mode())

# print(len(df.query("phone == 'Apple' & city == 'Vladivostok'")) / len(df) * 100)

# определите сколько всего было отправлено СМС, а затем расcчитайте отношение отправленных смс клиента к общему количеству. Столбец назовите sms_volume. Оставьте TOP-3
# df["sms_volume"] = df.sms / df.sms.sum()
# print(df.sort_values("sms_volume", ascending=False).head(3))
# print(df.nlargest(3, "sms_volume"))

# print(df.loc[df["city"] == "Vladivostok"].age.mean())
# print(df.loc[df["city"] == "Kazan"].age.mean() > df.loc[df["city"] == "Vladivostok"].age.mean())

# df["snn"] = df['surname'].str.upper() + "_" + df['name'].str.upper()
# df = df.set_index("snn")
# df = df.drop(columns=["name", "surname"])
# print(df)

print()