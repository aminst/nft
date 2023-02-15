import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import datetime

sns.set_theme(style="darkgrid")

with open('avg_degree_per_month.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

sorted_dates = sorted(obj)
x = []
y = []
counter = 0

for date in sorted_dates:
    x.append(counter)
    y.append(obj[date])
    counter += 1

data = pd.DataFrame(
    {'Months Passed': x,
     'Average Degree': y,
    })

g_results = sns.lineplot(x="Months Passed", y="Average Degree", data=data, lw=2)
plt.show()