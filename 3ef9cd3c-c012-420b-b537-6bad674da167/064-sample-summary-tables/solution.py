# Срез от Египет до Индия
temp_by_country_city_vs_year.loc["Египет":"Индия"]

# Срез от Египет, Каир до Индия, Дели
temp_by_country_city_vs_year.loc[("Египет", "Каир"):("Индия", "Дели")]

# Срез в обоих направлениях одновременно
temp_by_country_city_vs_year.loc[("Египет", "Каир"):("Индия", "Дели"), "2005":"2010"]