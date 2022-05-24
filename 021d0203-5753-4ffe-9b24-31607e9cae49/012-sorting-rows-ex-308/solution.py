# Отсортируйте census по регионам, затем по убыванию family_members
census_reg_fam = census.sort_values(["region", "family_members"], ascending=[True, False])

# Распечатайте первые несколько строк: census_reg_fam
print(census_reg_fam.head())