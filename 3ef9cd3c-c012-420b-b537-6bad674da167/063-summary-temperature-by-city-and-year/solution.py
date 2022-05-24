# Добавьте столбец year в temperatures
temperatures["year"] = temperatures["date"].dt.year

# Сводная таблица avg_temp_c по country и city в year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")

# Распечатайте результат
print(temp_by_country_city_vs_year)