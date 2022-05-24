import pandas as pd
temperatures = pd.read_csv("temperatures.csv")
temperatures['date'] = pd.to_datetime(temperatures['date'], errors='coerce')