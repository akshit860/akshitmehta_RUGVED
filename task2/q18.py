import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)
outs=deliveries[deliveries["player_dismissed"].notna()].groupby("player_dismissed").size()
average=deliveries.groupby("batsman")["batsman_runs"].sum().div(outs).dropna().sort_values(ascending=False)
print("18.",average.head(10))
pd.crosstab(matches["season"],matches["toss_decision"]).plot(kind="bar")
plt.title("Toss Decisions Across Seasons")
plt.xlabel("Season")
plt.ylabel("Number of Tosses")
plt.show()