# Импортируйте numpy с названием np
import numpy as np

# Получите среднее значение и медиану weekly_sales для каждого типа магазинов
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

# Распечатайте mean_med_sales_by_type
print(mean_med_sales_by_type)