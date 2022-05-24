# Создайте indiv_per_10k, содержащий число одиноких на десять тысяч человек в каждом регионе
census["indiv_per_10k"] = 10000 * census["individuals"] / census["city_pop"] 

# Фильтр для строк indiv_per_10k больше 20 
high_census = census[census["indiv_per_10k"] > 20]

# Отсортируйте high_census по убыванию indiv_per_10k
high_census_srt = high_census.sort_values("indiv_per_10k", ascending=False)

# Из high_census_srt выберите столбцы city и indiv_per_10k
result = high_census_srt[["city", "indiv_per_10k"]]

# Распечатайте результат
print(result)