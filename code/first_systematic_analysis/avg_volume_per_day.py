import sys
import os
import csv
import json

TX_VALUE_INDEX = 14

def write_volume_to_json(filename, volume):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(volume))

if __name__ == "__main__": # usage: python avg_volume_day.py <path_to_csv_day_files>
    filenames = os.listdir(sys.argv[1])

    volume_per_date = dict()

    for filename in filenames:
        print("READ ", filename)
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        volume_per_date[filename.split('.')[0]] = 0
        count = 0
        for row in reader:
            value = float(row[TX_VALUE_INDEX]) if row[TX_VALUE_INDEX] != 'null' else 0
            volume_per_date[filename.split('.')[0]] += value
            count += 1
        volume_per_date[filename.split('.')[0]] /= count
        print("DONE ", filename)
    
    write_volume_to_json('results/avg_volume_per_day.json', volume_per_date)