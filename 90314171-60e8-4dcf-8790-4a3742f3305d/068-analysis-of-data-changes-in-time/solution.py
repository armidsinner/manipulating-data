# Импортируйте matplotlib.pyplot с псевдонимом plt
import matplotlib.pyplot as plt

# Получите общее количество яблок, проданных на каждую дату
nb_sold_by_date = apples.groupby("date")["nb_sold"].sum()

# Создайте график количества проданных яблок по дате
nb_sold_by_date.plot(kind="line")

# Покажите график
plt.show()