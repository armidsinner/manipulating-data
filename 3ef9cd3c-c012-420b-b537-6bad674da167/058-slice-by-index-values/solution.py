# Отсортируйте индекс temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Получите выборку от Пакистан до Россия
print(temperatures_srt.loc["Пакистан":"Россия"])

# Получите выборку от Лахоре до Москва
print(temperatures_srt.loc["Лахоре":"Москва"])

# Получите выборку от Пакистан, Лахоре до Россия, Москва
print(temperatures_srt.loc[("Пакистан", "Лахоре"):("Россия", "Москва")])