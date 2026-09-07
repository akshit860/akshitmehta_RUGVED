import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)


run_wins = matches[matches["win_by_runs"] > 0]

highest = run_wins["win_by_runs"].max()
lowest = run_wins["win_by_runs"].min()

highest_match = run_wins[run_wins["win_by_runs"] == highest]
lowest_match = run_wins[run_wins["win_by_runs"] == lowest]

print("Venue where the highest run victory occurred:")
print(highest_match[["venue", "winner", "win_by_runs"]].to_string(index=False))

print("\nVenue where the lowest run victory occurred:")
print(lowest_match[["venue", "winner", "win_by_runs"]].to_string(index=False))