# Используйте логические условия temperatures для строк в 2010 и 2011 годах
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Установите date в качестве индекса и отсортируйте индекс
temperatures_ind = temperatures.set_index("date").sort_index()

# Используйте .loc[] для выборки temperatures для строк в 2010 и 2011 годах
print(temperatures_ind.loc["2010":"2011"])

# Используйте .loc[] для выборки temperatures_ind с августа 2010 года по февраль 2011 года
print(temperatures_ind.loc["2010-08":"2011-02"])