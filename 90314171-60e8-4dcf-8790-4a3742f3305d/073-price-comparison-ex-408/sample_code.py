# Измените количество ячеек до 20
apples[apples["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Измените количество ячеек до 20
apples[apples["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Добавьте к графику название "обычный" и "органический"
plt.legend(["обычный", "органический"])

# Покажите график
plt.show()