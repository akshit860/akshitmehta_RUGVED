import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

teams = []
for i in range(len(matches)):
    t1 = matches['team1'][i]
    t2 = matches['team2'][i]
    if t1 not in teams:
        teams.append(t1)
    if t2 not in teams:
        teams.append(t2)


win_rates = []
for team in teams:
    total = 0
    won = 0
    for i in range(len(matches)):
        if matches['team1'][i] == team or matches['team2'][i] == team:
            total = total + 1
        if matches['winner'][i] == team:
            won = won + 1
    rate = (won / total) * 100
    win_rates.append(rate)


for i in range(len(teams)):
    print(teams[i], ":", round(win_rates[i], 1), "%")


plt.figure(figsize=(9, 7))
plt.barh(teams, win_rates)
plt.title("Win Rate by Team")
plt.xlabel("Win Rate (%)")
plt.tight_layout()
plt.show()