# Рассчитайте общий объем продаж за неделю
sales_all = sales["weekly_sales"].sum()

# Рассчитайте объем еженедельных продаж для type A
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Рассчитайте объем еженедельных продаж для type B
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Рассчитайте объем еженедельных продаж для type C
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Рассчитайте долю продаж для каждого типа
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)