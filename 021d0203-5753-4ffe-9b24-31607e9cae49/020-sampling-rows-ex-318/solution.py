# Фильтр для строк, где family_members меньше 1000 и region UFO
fam_lt_1k_pac = census[(census["family_members"] < 1000) & (census["region"] == "UFO")]

# Распечатайте результат
print(fam_lt_1k_pac)