# Получите среднее значение weekly_sales по столбцам type и is_holiday  
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Распечатайте mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)