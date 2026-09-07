import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

player_counts = matches["player_of_match"].value_counts()

players = player_counts[player_counts > 3]

print("Players who won Player of the Match more than 3 times:")
print(players)