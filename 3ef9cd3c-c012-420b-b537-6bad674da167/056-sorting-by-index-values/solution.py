# Отсортируйте temperatures_ind по значениям индекса
print(temperatures_ind.sort_index())

# Отсортируйте temperatures_ind по значениям индексов на уровне city
print(temperatures_ind.sort_index(level="city"))

# Отсортируйте temperatures_ind по country затем по убыванию city
print(temperatures_ind.sort_index(level=["country", "city"], ascending = [True, False]))