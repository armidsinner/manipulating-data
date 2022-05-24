# Получите 23-ю строку, 2-й столбец (index 22, 1)
print(temperatures.iloc[22, 1])

# Получите первые 5 строк
print(temperatures.iloc[:5])

# Получите все строки, столбцы 3 и 4
print(temperatures.iloc[:, 2:4])

# Используйте срез в обоих направлениях одновременно
print(temperatures.iloc[:5, 2:4])