import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import datetime

sns.set_theme(style="darkgrid")

with open('tx_usd_per_day.json', 'r') as myfile:
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
    {'Days Passed': x,
     'Value of Transactions (USD)': y,
    })

g_results = sns.lineplot(x="Days Passed", y="Value of Transactions (USD)", data=data, lw=2)
# g_results.set(xscale='log')
plt.show()
