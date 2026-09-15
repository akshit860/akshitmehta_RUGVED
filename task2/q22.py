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


toss_wins = []
for team in teams:
    count = 0
    for i in range(len(matches)):
        if matches['toss_winner'][i] == team:
            count = count + 1
    toss_wins.append(count)

for i in range(len(teams)):
    print(teams[i], ":", toss_wins[i])


plt.figure(figsize=(9, 7))
plt.barh(teams, toss_wins)
plt.title("Toss Wins by Team")
plt.xlabel("Number of Tosses Won")
plt.tight_layout()
plt.show()