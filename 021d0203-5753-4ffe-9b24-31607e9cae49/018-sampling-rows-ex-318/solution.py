# Отфильтруйте строки, в которых количество отдельных лиц превышает 10000
ind_gt_10k = census[census["individuals"] > 10000]

# Распечатайте результат
print(ind_gt_10k)