# Получите среднее значение weekly_sales для каждого типа магазинов
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Распечатайте mean_sales_by_type
print(mean_sales_by_type)