import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("deliveries.csv")
deliveries = pd.read_csv(csv_path)

sixes = deliveries[deliveries["batsman_runs"] == 6]

print("Deliveries where the batsman scored a six:")
print(sixes[["match_id", "inning", "over", "ball", "batsman", "bowler", "batsman_runs"]])