import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)
total_runs = deliveries.groupby("batsman")["batsman_runs"].sum()

dismissals = deliveries[deliveries["player_dismissed"].notna()]
dismissal_counts = dismissals.groupby("player_dismissed").size()

batting_average = total_runs / dismissal_counts

batting_average = batting_average.dropna()

top_10 = batting_average.sort_values(ascending=False).head(10)

print("Top 10 batsmen by batting average:")
print(top_10)