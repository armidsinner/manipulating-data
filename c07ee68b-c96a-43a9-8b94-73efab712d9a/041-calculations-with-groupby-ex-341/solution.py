# Сгруппируйте по типу и рассчитайте общий объем продаж за неделю
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Рассчитайте долю продаж для каждого типа
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)