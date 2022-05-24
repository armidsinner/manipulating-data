# Добавьте новый столбец total, содержащий сумму столбцов individuals и family_members
census["total"] = census["individuals"] + census["family_members"]

# Добавьте новый столбец p_individuals, содержащий долю individuals для каждого региона
census["p_individuals"] = census["individuals"] / census["total"]

# Распечатайте результат
print(census)