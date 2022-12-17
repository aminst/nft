import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import datetime


with open('tx_count_per_day.json', 'r') as myfile:
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

dframe = pd.DataFrame(
    {'Days after mint': x,
     'Number of TXs': y,
    })

sns.lineplot(data=dframe, x="Days after mint", y="Number of TXs")

plt.show()
