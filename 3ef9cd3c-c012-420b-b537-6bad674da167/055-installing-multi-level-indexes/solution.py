# Установите индекс temperatures для country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# Список кортежей: Бразилия, Рио-де-Жанейро & Пакистан, Лахор
rows_to_keep = [("Бразилия", "Рио-де-Жанейро"), ("Пакистан", "Лахор")]

# Подмножество для строк, которые нужно сохранить
print(temperatures_ind.loc[rows_to_keep])