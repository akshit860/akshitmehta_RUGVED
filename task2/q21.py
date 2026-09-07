import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

winner_counts = matches["winner"].value_counts()

print("Distribution of teams that won matches:")
print(winner_counts)

winner_counts.plot(kind="bar")

plt.title("Distribution of Teams That Won Matches")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()