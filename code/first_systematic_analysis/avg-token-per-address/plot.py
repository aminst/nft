import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

sns.set_theme(style="darkgrid")

with open('avg_token_per_address.json', 'r') as myfile:
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
     'Avgerage Token per Address': y,
    })

sns.lineplot(x="Days Passed", y="Avgerage Token per Address", data=data, lw=2)
plt.show()

# too har rooz ye average token per address hast. hala bar asas har rooz in meghdar ro keshidim.