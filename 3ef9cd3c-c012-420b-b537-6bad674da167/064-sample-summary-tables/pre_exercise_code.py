import pandas as pd
temperatures = pd.read_csv("temperatures.csv")

temperatures['date'] = pd.to_datetime(temperatures['date'], errors='coerce')
temperatures["year"] = temperatures["date"].dt.year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")