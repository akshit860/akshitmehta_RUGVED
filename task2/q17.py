import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

wickets=deliveries[deliveries["player_dismissed"].notna()]
wickets=wickets[~wickets["dismissal_kind"].isin(["run out","retired hurt","obstructing the field"])]
print(wickets.groupby("bowler").size().sort_values(ascending=False))