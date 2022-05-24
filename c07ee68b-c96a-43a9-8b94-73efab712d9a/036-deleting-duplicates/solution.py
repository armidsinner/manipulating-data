# Удалите дубликаты строк комбинации store/type
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Удалите дубликаты строк комбинации store/department
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Выберите строки, is_holiday = True, и удалите повторяющиеся даты
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Распечатайте столбец date в holiday_dates
print(holiday_dates["date"])