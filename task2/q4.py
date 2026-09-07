import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

toss_decisions = matches.groupby(
    ["toss_winner", "toss_decision"]
).size()

print("Toss decisions taken by each team:")
print(toss_decisions)