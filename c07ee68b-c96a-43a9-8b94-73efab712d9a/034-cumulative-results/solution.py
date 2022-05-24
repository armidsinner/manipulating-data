# Отсортируйте строки sales_1_1 по столбцу date
sales_1_1 = sales_1_1.sort_values("date")

# Получите сумму еженедельных продаж, добавив в cum_weekly_sales
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Получите максимальную сумму weekly_sales и добавьте ее в столбец cum_max_sales
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# Распечатайте столбцы, которые вы рассчитали
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])