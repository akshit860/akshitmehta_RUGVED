import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

match_runs = deliveries.groupby("match_id")["total_runs"].sum().reset_index()

match_runs = match_runs.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

season_runs = match_runs.groupby("season")["total_runs"].sum()

print("Total runs scored in each season:")
print(season_runs)