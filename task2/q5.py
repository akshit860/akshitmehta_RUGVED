import pandas as pd
from pathlib import Path

csv_path = Path(__file__).with_name("matches.csv")
matches = pd.read_csv(csv_path)

result_counts = matches["result"].value_counts()

print("Match results:")
print(result_counts)