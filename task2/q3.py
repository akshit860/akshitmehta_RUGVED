import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

city_counts = matches["city"].value_counts()

print("Total matches conducted city-wise:")
print(city_counts)