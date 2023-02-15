import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

sns.set_theme(style="darkgrid")

with open('out.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

sorted_data = sorted(obj)
number_of_unique_values = dict()
counter = 0

for address in sorted_data:
    if obj[address] not in number_of_unique_values.keys():
        number_of_unique_values[obj[address]] = 0
    
    number_of_unique_values[obj[address]] += 1

total = sum(number_of_unique_values.values())
distribution_of_unique_values = {key: value / total for key, value in number_of_unique_values.items()}

cdf = dict()
total = 0.0

for key in sorted(distribution_of_unique_values):
    total += distribution_of_unique_values[key]
    cdf[key] = total

del cdf[0]

data = pd.DataFrame(
    {'Degree Centrality': list(cdf.keys()),
     'CDF': list(cdf.values()),
    })

g_results = sns.lineplot(x="Degree Centrality", y="CDF", data=data, lw=2)
plt.ylim(0, 1.02)
g_results.set(xscale='log')
plt.show()



# be ezaye har node ye meghdar darim. miaym distributionesh ro mikeshim