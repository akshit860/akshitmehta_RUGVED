import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)


teams = pd.unique(matches[["team1", "team2"]].values.ravel())

data = []

for team in teams:
    total_matches = ((matches["team1"] == team) | (matches["team2"] == team)).sum()
    winning_matches = (matches["winner"] == team).sum()
    win_rate = (winning_matches / total_matches) * 100

    data.append([team, total_matches, winning_matches, win_rate])

team_data = pd.DataFrame(
    data,
    columns=["Team", "Total Matches", "Winning Matches", "Win Rate"]
)

print(team_data)

team_data.plot(
    x="Team",
    y=["Total Matches", "Winning Matches"],
    kind="bar"
)

plt.title("Total Matches vs Winning Matches")
plt.xlabel("Teams")
plt.ylabel("Number of Matches")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

team_data.plot(
    x="Team",
    y="Win Rate",
    kind="bar"
)

plt.title("Win Rate of All Teams")
plt.xlabel("Teams")
plt.ylabel("Win Rate (%)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()