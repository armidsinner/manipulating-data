# Выведите среднее значение weekly_sales по department и type; заполните недостающие значения 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))