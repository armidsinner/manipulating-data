# Пользовательская функция IQR
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Распечатайте IQR столбцы temperature_c, fuel_price_usd_per_l, и unemployment
print(sales[["temperature_c", ____, ____]].agg(iqr))