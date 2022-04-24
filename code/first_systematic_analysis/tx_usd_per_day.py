import sys
import os
import csv
import json
import pandas as pd

TX_VALUE_INDEX = 14

def write_volume_to_json(filename, volume):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(volume))

def get_USD_exchange_value(timestamp, price_df):
    matched_data = price_df.loc[price_df['date'] == timestamp]
    if len(matched_data):
        matched_data = matched_data.iloc[0]
        return matched_data['open']
    else:
        return 1

if __name__ == "__main__": # usage: python tx_usd_per_day.py <path_to_csv_day_files> <usd_file>
    filenames = os.listdir(sys.argv[1])
    usd_file = sys.argv[2]

    price_df = pd.read_csv(usd_file)

    usd_per_date = dict()

    for filename in filenames:
        print("READ ", filename)
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        time = filename.split('.')[0]
        usd_per_date[time] = 0
        usd = get_USD_exchange_value(time, price_df)
        for row in reader:
            value = float(row[TX_VALUE_INDEX]) if row[TX_VALUE_INDEX] != 'null' else 0
            usd_per_date[time] += value * usd
        print("DONE ", filename)
    
    write_volume_to_json('results/tx_usd_per_day.json', usd_per_date)