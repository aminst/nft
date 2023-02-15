import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

sns.set_theme(style="darkgrid")

with open('outdegree.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

total = sum(obj.values())
distribution = {key: value / total for key, value in obj.items()}
distribution = {int(k):float(v) for k,v in distribution.items()}

cdf = dict()
total = 0.0

for key in sorted(distribution):
    total += distribution[key]
    cdf[key] = total

del cdf[0]

data = pd.DataFrame(
    {'Outdegree': list(cdf.keys()),
     'CDF': list(cdf.values()),
    })

g_results = sns.lineplot(x="Outdegree", y="CDF", data=data, lw=2)
plt.ylim(0, 1.02)
g_results.set(xscale='log')
plt.show()



# be ezaye har node ye meghdar darim. miaym distributionesh ro mikeshim