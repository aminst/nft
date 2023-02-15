import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import datetime

sns.set_theme(style="darkgrid")

with open('throug_time_results.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

for key in obj:
    obj[key] = obj[key]["assortivity"]

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
     'Average Assortivity': y,
    })

g_results = sns.lineplot(x="Months Passed", y="Average Assortivity", data=data, lw=2)
plt.show()