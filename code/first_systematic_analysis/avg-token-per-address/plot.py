import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import datetime


import numpy as np
import scipy.stats

with open('avg_token_per_address.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

sorted_dates = sorted(obj)
x = []
y = []
counter = 0


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h


for date in sorted_dates:
    if counter % 10 == 0:
        x.append(counter)
        y.append(obj[date])
    counter += 1

dframe = pd.DataFrame(
    {'Days after mint': x,
     'Average Token': y,
    })

sns.lineplot(data=dframe, x="Days after mint", y="Average Token")

# m, lower_bound, upper_bound = mean_confidence_interval(dframe["Average Token"])
# print(lower_bound)
# plt.fill_between(dframe["Days after mint"], lower_bound, upper_bound, alpha=.3)
plt.show()
