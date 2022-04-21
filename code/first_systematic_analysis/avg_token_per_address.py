import sys
import os
import csv
import json

FROM_IDX = 5
TO_IDX = 8
TOKEN_ADDRESS_IDX = 9
TOKEN_ID_IDX = 10

def write_avg_token_to_json(filename, avg_token):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(avg_token))

if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])

    nfts = set()

    avg_zero_out_in_diff = dict()

    prev = 0
    for filename in filenames:
        print("READ ", filename)
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        time = filename.split('.')[0]
        for row in reader:
            if row[FROM_IDX] == '0x0000000000000000000000000000000000000000':
                prev += 1
            elif row[TO_IDX] == '0x0000000000000000000000000000000000000000':
                prev -= 1
            nfts.add(row[TOKEN_ADDRESS_IDX] + ':' + row[TOKEN_ID_IDX])
        avg_zero_out_in_diff[time] = prev / len(nfts)
        print("DONE ", filename)
    
    write_avg_token_to_json('results/avg_token_per_address.json', avg_zero_out_in_diff)