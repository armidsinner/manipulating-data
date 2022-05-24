# Удалите дубликаты строк комбинации store/type
store_types = ____
print(store_types.head())

# Удалите дубликаты строк комбинации store/department
store_depts = ____
print(store_depts.head())

# Выберите строки, is_holiday = True, и удалите повторяющиеся даты
holiday_dates = sales[sales[____]].drop_duplicates(____)

# Распечатайте столбец date в holiday_dates
print(____)