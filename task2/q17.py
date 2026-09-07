import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

dismissals = deliveries[deliveries["player_dismissed"].notna()]

wickets = dismissals.groupby("bowler").size()

wickets = wickets.sort_values(ascending=False)

print("Total wickets taken by each bowler:")
print(wickets)