# Измените прозрачность гистограммы на 0.5 
apples[apples["type"] == "conventional"]["avg_price"].hist()

# Измените прозрачность гистограммы на 0.5
apples[apples["type"] == "organic"]["avg_price"].hist()

# Добавьте к графику название "обычный" и "органический"
plt.legend(["обычный", "органический"])

# Покажите график
plt.show()