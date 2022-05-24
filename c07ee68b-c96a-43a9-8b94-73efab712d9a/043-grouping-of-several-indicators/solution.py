# Импортируйте numpy с названием np
import numpy as np

# Получите weekly_sales для каждого типа магазинов: получите min, max, mean, и median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Распечатайте sales_stats
print(sales_stats)

# Получите unemployment и fuel_price_usd_per_l для каждого типа магазинов: получите min, max, mean, и median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Распечатайте unemp_fuel_stats
print(unemp_fuel_stats)