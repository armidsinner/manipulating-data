import pandas as pd
sales = pd.read_csv("sales_subset.csv")

# Удалите дубликаты строк комбинации store/type
store_types = sales.drop_duplicates(subset=["store", "type"]).reset_index(drop=True)

# Удалите дубликаты строк комбинации store/department
store_depts = sales.drop_duplicates(subset=["store", "department"]).reset_index(drop=True)

del sales