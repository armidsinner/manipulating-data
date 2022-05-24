# Распечатайте первые несколько строк: sales
print(sales.head())

# Распечатайте информацию о продажах
print(sales.info())

# Распечатайте среднее значение еженедельных продаж
print(sales["weekly_sales"].mean())

# Распечатайте медиану еженедельных продаж
print(sales["weekly_sales"].median())