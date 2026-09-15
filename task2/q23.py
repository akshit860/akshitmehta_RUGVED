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

wins = []
for team in teams:
    count = 0
    for i in range(len(matches)):
        if matches['winner'][i] == team:
            count = count + 1
    wins.append(count)

n = len(teams)
for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if wins[j] > wins[max_index]:
            max_index = j
    temp_w = wins[i]
    wins[i] = wins[max_index]
    wins[max_index] = temp_w
    temp_t = teams[i]
    teams[i] = teams[max_index]
    teams[max_index] = temp_t

top5_teams = teams[0:5]
top5_wins = wins[0:5]

print(top5_teams)
print(top5_wins)

# Step 5: chart
plt.figure(figsize=(8, 5))
plt.barh(top5_teams, top5_wins)
plt.title("Top 5 Teams by Total Wins")
plt.xlabel("Number of Wins")
plt.tight_layout()
plt.show()