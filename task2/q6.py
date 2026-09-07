import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

tied_matches = matches[matches["result"] == "tie"]

print("Teams involved in tied matches:")
print(tied_matches[["team1", "team2"]])