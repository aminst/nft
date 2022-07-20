import json
import pandas as pd
import numpy as np
import networkx as nx
import os

filenames = os.listdir('data')
sorted_filenames = sorted(filenames)
results = dict()
txs = None
for filename in sorted_filenames:
    print("READ" + filename)
    txs = pd.read_csv('data/' + filename, header=None)
    net = nx.from_pandas_edgelist(txs, 5, 8, create_using=nx.DiGraph())
    if filename not in results:
        results[filename] = dict()
    results[filename]['avg_clustering'] = nx.average_clustering(net)
    results[filename]['assortivity'] = nx.degree_assortativity_coefficient(net)
    try:
        results[filename]['avg_path_length'] = nx.average_shortest_path_length(net)
    except:
        results[filename]['avg_path_length'] = -1

json.dump(results, open('time_results.json', 'w'))
