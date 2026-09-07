import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

mean_runs = matches["win_by_runs"].mean()
median_runs = matches["win_by_runs"].median()
std_runs = matches["win_by_runs"].std()

print("Mean:", mean_runs)
print("Median:", median_runs)
print("Standard Deviation:", std_runs)