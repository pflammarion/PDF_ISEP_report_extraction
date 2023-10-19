import json
import os

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


file = 'output/monfile.csv'

df = pd.read_csv(file, header=0)

df["demand_score"] = 3 * df["Choix 1"] + 2 * df["Choix 2"] + 1 * df["Choix 3"]
df["difficulty"] = df["demand_score"] / df["Quota"]


df_sorted = df.sort_values(by='Choix 1', ascending=False)

number_choice = 10
df_filtered = df_sorted[:number_choice]

df_filtered = df_filtered.sort_values(by='difficulty')

colors = list(mcolors.TABLEAU_COLORS.values())  # You can add more colors as needed

# Plotting the bar plot for 'Affectation' and 'Choix 1' with colors
ax = df_filtered.plot(x='difficulty', y='demand_score', kind='bar', color=colors)

plt.xlabel('Difficulty score')
plt.ylabel('Demand score')
plt.title('Correlation between difficulty and demand score in 2019')

# Adding custom legend
for i, label in enumerate(df_filtered['Destination']):
    ax.bar(0, 0, color=colors[i], label=label)

plt.legend(loc='upper right')
plt.show()


