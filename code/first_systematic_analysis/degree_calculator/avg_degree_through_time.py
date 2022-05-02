import sys
import os
import csv
import json

FROM_IDX = 5
TO_IDX = 8

def write_avg_degree_to_json(filename, avg_degree):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(avg_degree))

if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])
    sorted_filenames = sorted(filenames)

    addresses = set()
    avg_degree = dict()

    prev_degree_count = 0
    for filename in sorted_filenames:
        print("READ ", filename)
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            prev_degree_count += 2
            addresses.add(row[FROM_IDX])
            addresses.add(row[TO_IDX])
        print("DONE ", filename)
        print(len(addresses))
        avg_degree[filename] = prev_degree_count / len(addresses)
    
    write_avg_degree_to_json('../results/avg_degree_per_month.json', avg_degree)
    

