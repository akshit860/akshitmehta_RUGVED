import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

match_runs = deliveries.groupby("match_id")["total_runs"].sum().reset_index()

match_runs = match_runs.merge(
    matches[["id", "venue"]],
    left_on="match_id",
    right_on="id"
)

average_runs = match_runs.groupby("venue")["total_runs"].mean()

print("Average runs scored at each venue:")
print(average_runs)