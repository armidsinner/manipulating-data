import pandas as pd
temperatures = pd.read_csv("temperatures.csv")

temperatures_ind = temperatures.set_index(["country", "city"])
temperatures_srt = temperatures_ind.sort_index()