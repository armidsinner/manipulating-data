# Выведите среднее значение weekly_sales по department и type; 
# Заполните недостающие значения 0; суммируя all rows и cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", ____))