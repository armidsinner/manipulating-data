import pandas as pd
temperatures = pd.read_csv("temperatures.csv")

temperatures_ind = temperatures.set_index(["country", "city"])