# Гистограмма conventional avg_price 
apples[apples["type"] == "conventional"]["avg_price"].hist()

# Гистограмма organic avg_price
apples[apples["type"] == "organic"]["avg_price"].hist()

# Добавьте к графику название "обычный" и "органический"
plt.legend(["обычный", "органический"])

# Покажите график
plt.show()