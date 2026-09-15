import pandas as pd
matches=pd.read_csv("matches.csv")
winners=matches["winner"].value_counts()
print(winners.to_string())