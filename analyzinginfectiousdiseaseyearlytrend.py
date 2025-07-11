# -*- coding: utf-8 -*-
"""AnalyzingInfectiousDiseaseYearlyTrend.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12p5J9kw-EWF4_IO8mUUldHS4_qSkqe37
"""

import matplotlib.pyplot as plt
import pandas as pd
from google.colab import files

uploaded = files.upload()

data = pd.read_csv("Infectious Disease 2001-2014.csv")

data.head()

grouped_data = data.groupby(["Year","Disease"])[["Count"]].sum()

top_disease_count = grouped_data.groupby("Year", group_keys=False).apply(lambda x: x.nlargest(3,"Count"))

for year in grouped_data.index.get_level_values("Year").unique():
  top_count_disease = top_disease_count[top_disease_count.index.get_level_values("Year")==year]
  print(f"Top 3 Diseases by Count for {year}:")
  for idx, row in top_count_disease.iterrows():
    disease = row.name[1]
    count = row["Count"]
    print(f"{disease} (Count: {count})")

top_disease_count = grouped_data.groupby("Year", group_keys=False).apply(lambda x: x.nlargest(3,"Count")).reset_index()
plt.figure(figsize=(12,6))
for year in top_disease_count["Year"].unique():
  year_data = top_disease_count[top_disease_count["Year"]==year]
  plt.scatter(year_data["Year"],year_data["Count"], label=f"Top Disease in Year {year}")
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Top Disease by Count for Each Year")
plt.legend()
plt.grid(True)
plt.show()