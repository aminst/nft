import sys
import os
import json

def write_line_count_to_json(filename, line_count):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(line_count))

if __name__ == "__main__": # usage: python tx_per_day.py <path_to_csv_day_files>
    filenames = os.listdir(sys.argv[1])

    line_count = dict()

    for filename in filenames:
        print("READ ", filename)
        count = len(open(sys.argv[1] + '/' + filename, 'r').readlines())
        line_count[filename.split('.')[0]] = count
        print("DONE ", filename)
    
    write_line_count_to_json('results/tx_count_per_day.json', line_count)