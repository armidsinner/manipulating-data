# Отсортируйте census по количеству family_members в порядке убывания
census_fam = census.sort_values("family_members", ascending=False)

# Распечатайте первые несколько строк: census_fam
print(census_fam.head())