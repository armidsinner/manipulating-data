# Импортируйте matplotlib.pyplot с псевдонимом plt
import matplotlib.pyplot as plt

# Распечатайте первые несколько строк данных
print(apples.head())

# Получите общее количество проданных яблок каждого размера
nb_sold_by_size = apples.groupby("size")["nb_sold"].sum()

# Создайте столбчатый график количества проданных яблок по размеру
nb_sold_by_size.plot(kind="bar")

# Покажите график
plt.show()