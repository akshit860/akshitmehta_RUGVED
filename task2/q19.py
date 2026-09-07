import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

toss_data = pd.crosstab(
    matches["season"],
    matches["toss_decision"]
)

toss_data.plot(kind="bar")

plt.title("Toss Decisions Across Seasons")
plt.xlabel("Season")
plt.ylabel("Number of Toss Decisions")
plt.xticks(rotation=45)
plt.legend(title="Toss Decision")
plt.tight_layout()

plt.show()