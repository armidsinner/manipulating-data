import pandas as pd
temperatures = pd.read_csv("temperatures.csv")

temperatures.sample(frac=1).reset_index(drop=True)
temperatures_ind = temperatures.set_index(["country", "city"])