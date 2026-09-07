import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)
toss_outcomes = pd.crosstab(
    matches["toss_winner"],
    matches["toss_decision"]
)

print("Toss outcomes of all teams:")
print(toss_outcomes)

toss_outcomes.plot(kind="bar")

plt.title("Toss Outcomes of All Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Toss Decisions")
plt.xticks(rotation=90)
plt.legend(title="Toss Decision")
plt.tight_layout()

plt.show()