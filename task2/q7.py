import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

run_wins = matches[matches["win_by_runs"] > 0]

highest = run_wins["win_by_runs"].max()
lowest = run_wins["win_by_runs"].min()

highest_team = run_wins[run_wins["win_by_runs"] == highest]["winner"]
lowest_team = run_wins[run_wins["win_by_runs"] == lowest]["winner"]

print("Team with highest win by runs:")
print(highest_team.to_string(index=False))
print("Runs:", highest)

print("\nTeam with lowest win by runs:")
print(lowest_team.to_string(index=False))
print("Runs:", lowest)