import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

pd.crosstab(matches["toss_winner"],matches["toss_decision"]).plot(kind="bar")
plt.title("Toss Outcomes of All Teams")
plt.xlabel("Team")
plt.ylabel("Number of Tosses")
plt.xticks(rotation=75)
plt.show()