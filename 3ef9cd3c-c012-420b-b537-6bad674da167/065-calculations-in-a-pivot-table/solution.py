# Получить среднюю температуру по всему миру по годам
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Фильтр для года, в котором была самая высокая средняя температура
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Получить среднюю температуру по городам
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Фильтр для города с самой низкой средней температурой
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])