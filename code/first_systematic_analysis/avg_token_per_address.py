import sys
import os
import csv
import json

FROM_IDX = 5
TO_IDX = 8

def write_avg_token_to_json(filename, avg_token):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(avg_token))

if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])
    sorted_filenames = sorted(filenames)
    print(sorted_filenames)

    addresses = set()

    avg_zero_out_in_diff = dict()

    prev = 0
    for filename in sorted_filenames:
        print("READ ", filename)
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        time = filename.split('.')[0]
        for row in reader:
            if row[FROM_IDX] == '0x0000000000000000000000000000000000000000':
                prev += 1
            elif row[TO_IDX] == '0x0000000000000000000000000000000000000000':
                prev -= 1
            from_address = row[FROM_IDX]
            to_address = row[TO_IDX]
            if from_address != '0x0000000000000000000000000000000000000000':
                addresses.add(from_address)
            if to_address != '0x0000000000000000000000000000000000000000':
                addresses.add(to_address)
            
        avg_zero_out_in_diff[time] = prev / len(addresses)
        print("DONE ", filename)
    
    write_avg_token_to_json('results/avg_token_per_address.json', avg_zero_out_in_diff)