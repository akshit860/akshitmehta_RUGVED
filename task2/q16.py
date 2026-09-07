import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

batsman_runs = deliveries.groupby("batsman")["batsman_runs"].sum()

top_10 = batsman_runs.sort_values(ascending=False).head(10)

print("Top 10 batsmen by total runs:")
print(top_10)