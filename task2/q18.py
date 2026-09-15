import pandas as pd
deliveries=pd.read_csv("deliveries.csv")

runs_per_batsman= deliveries.groupby("batsman")["batsman_runs"].sum()
dismissals=deliveries[deliveries["player_dismissed"].notna() & deliveries["dismissal_kind"]!="retired hurt"]
times_out=dismissals.groupby("player_dismissed").size()

avg_run_batsman=runs_per_batsman / times_out
print(avg_run_batsman.dropna().sort_values(ascending=False).head(10))