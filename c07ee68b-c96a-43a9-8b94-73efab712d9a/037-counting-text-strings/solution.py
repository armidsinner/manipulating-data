# Подсчитайте количество stores каждого type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Посчитайте долю stores каждого type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Подсчитайте количество номеров department и отсортируйте
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Подсчитайте количество номеров departments и отсортируйте
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)