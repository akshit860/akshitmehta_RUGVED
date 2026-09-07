import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

top_5 = matches["winner"].value_counts().head(5)

print("Top 5 teams with most wins:")
print(top_5)

top_5.plot(kind="bar")

plt.title("Top 5 Teams with Most Wins Across All Seasons")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()