import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)
winner=matches["winner"].value_counts()

print("23.",winner.head(5))
winner.head(5).plot(kind="bar")
plt.title("Top 5 Teams With Most Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.show()