# Пользовательская функция IQR
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Распечатайте IQR столбца temperature_c
print(____)