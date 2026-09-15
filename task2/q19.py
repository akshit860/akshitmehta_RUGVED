import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

csv_path1 = Path(__file__).with_name("deliveries.csv")
csv_path2 = Path(__file__).with_name("matches.csv")
deliveries = pd.read_csv(csv_path1)
matches = pd.read_csv(csv_path2)

played=pd.concat([matches["team1"],matches["team2"]]).value_counts()
wins=matches["winner"].value_counts()
team=pd.DataFrame({"Total Matches":played,"Winning Matches":wins}).fillna(0)
team["Win Rate"]=team["Winning Matches"]/team["Total Matches"]*100
print("20.",team)
team[["Total Matches","Winning Matches"]].plot(kind="bar")
plt.title("Total Matches vs Winning Matches")
plt.xlabel("Team")
plt.ylabel("Matches")
plt.xticks(rotation=75)
plt.show()