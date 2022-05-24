import pandas as pd
sales = pd.read_csv("sales_subset.csv")
is_store_1 = sales["store"] == 1
is_dept_1 = sales["department"] == 1

sales_1_1 = sales[is_store_1 & is_dept_1].copy().sample(frac=1)