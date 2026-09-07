import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")

matches = pd.read_csv(csv_path)
city_counts = matches["city"].value_counts()

max_matches = city_counts.max()
min_matches = city_counts.min()

max_cities = city_counts[city_counts == max_matches]
min_cities = city_counts[city_counts == min_matches]

print("Cities with maximum matches:")
print(max_cities)

print("\nCities with minimum matches:")
print(min_cities)