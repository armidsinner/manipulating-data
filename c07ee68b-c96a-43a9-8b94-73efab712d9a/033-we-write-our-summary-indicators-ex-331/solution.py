# Импортируйте NumPy и создайте пользовательскую функцию IQR
import numpy as np

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Распечатайте IQR и медианы temperature_c, fuel_price_usd_per_l, и unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))