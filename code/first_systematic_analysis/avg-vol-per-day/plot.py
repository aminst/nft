import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

sns.set_theme(style="darkgrid")

with open('avg_volume_per_day.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

sorted_dates = sorted(obj)
x = []
y = []
counter = 0

for date in sorted_dates:
    if True:
        x.append(counter)
        y.append(obj[date])
    counter += 1

data = pd.DataFrame(
    {'Days Passed': x,
     'Average Volume (ETH)': y,
    })

sns.lineplot(x="Days Passed", y="Average Volume (ETH)", data=data, lw=2)
plt.show()

# too har rooz ye average volume hast. baraye har rooz keshidimesh