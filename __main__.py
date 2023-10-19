import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

df = pd.read_csv("output.csv", header=0)

df_sorted = df.sort_values(by='Choix 1', ascending=False)

print("----------------------")
print("Les destinations les plus demandées en choix 1 sont :")
print(df_sorted.loc[:, ['Destination', 'Choix 1']][:3])
print("----------------------")

number_choice = 10

df_choice = df_sorted.reset_index(drop=True)[:number_choice]

colors = list(mcolors.TABLEAU_COLORS.values())  # You can add more colors as needed

# Plotting the bar plot for 'Affectation' and 'Choix 1' with colors
ax = df_choice.plot(x='Affectation', y='Choix 1', kind='bar', color=colors)

plt.title('Correlation between Affectation and Choix 1')
plt.xlabel('Affectation')
plt.ylabel('Choix 1')


# Adding custom legend
for i, label in enumerate(df_choice['Destination']):
    ax.bar(0, 0, color=colors[i], label=label)

plt.legend(loc='upper right')
plt.show()


