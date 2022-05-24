# Распечатайте temperatures
print(temperatures)

# Установите индекс temperatures для city
temperatures_ind = temperatures.set_index("city")

# Распечатайте temperatures_ind
print(temperatures_ind)

# Сбросьте индекс, сохранив его содержимое
print(temperatures_ind.reset_index())

# Сбросьте индекс, удалив его содержимое
print(temperatures_ind.reset_index(drop=True))