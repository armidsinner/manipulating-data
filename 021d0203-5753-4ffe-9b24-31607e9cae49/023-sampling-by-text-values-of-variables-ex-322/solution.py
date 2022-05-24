# Города SFO (Сибирский федеральный округ)
sfo = ["Novosibirsk", "Angarsk", "Krasnoyarsk", "Norilsk"]

# Фильтр по городам SFO
sfo_census = census[census["city"].isin(sfo)]

# Распечатайте результат
print(sfo_census)