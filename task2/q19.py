import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualization():
    matches=pd.read_csv("matches.csv")
    season_results=matches.groupby(['season','toss_decision']).size().unstack()

    season_results.plot(kind="bar", stacked=True, figsize=(10,10))
    plt.title("Toss decision across all seasons")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
visualization()