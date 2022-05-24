# Составьте список городов, по которым нужно сделать подмножество
cities = ["Москва", "Санкт-Петербург"]

# Подмножество температур в квадратных скобках
print(temperatures[temperatures["city"].isin(cities)])

# Подмножество temperature_ind с использованием .loc[]
print(temperatures_ind.loc[cities])