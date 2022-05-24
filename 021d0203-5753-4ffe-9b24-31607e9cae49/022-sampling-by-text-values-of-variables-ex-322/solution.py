# Фильтр для строк SZFO или SKFO столбца region
szfo_skfo = census[(census["region"] == "SZFO") | (census["region"] == "SKFO")]

# Распечатайте результат
print(szfo_skfo)