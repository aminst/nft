import sys
import os
import csv
from datetime import datetime
import json
TIME_STAMP = 3
VALUE = 14

def dict_to_file(d, name):
    with open(name, 'w') as convert_file:
        convert_file.write(json.dumps(d))



if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])

    tokens = dict()

    for filename in filenames:
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            if row[VALUE] != 'null' and row[TIME_STAMP] != 'null':
                date = (datetime.today() - datetime.strptime(row[TIME_STAMP][:10], '%Y-%m-%d')).days
                if date in tokens:
                    tokens[date] += int(row[VALUE])
                else:
                    tokens[date] = int(row[VALUE])


        print("READ ", filename)

    dict_to_file(tokens, "market_value.json")
