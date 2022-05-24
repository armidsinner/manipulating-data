# С предыдущего шага
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Сгруппируйте sales по "type" и "is_holiday", получите сумму недельных продаж
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)