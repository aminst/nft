import sys
import os
import csv

TX_TIMESTAMP_IDX = 3

def extract_date(tx_timestamp):
    """
    Extracts the date from the transaction timestamp.
    """
    return tx_timestamp[:10]

if __name__ == "__main__": # usage: python date_extractor.py <path_to_csv_files> <output_folder>
    filenames = os.listdir(sys.argv[1])

    dates = dict()
    
    for filename in filenames:
        print("READ ", filename)
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            extracted_time = extract_date(row[TX_TIMESTAMP_IDX])
            if extracted_time not in dates:
                dates[extracted_time] = open(sys.argv[2] + '/' + extracted_time + '.csv', 'w')
                dates[extracted_time].write(','.join(row) + '\n')
            else:
                dates[extracted_time].write(','.join(row) + '\n')
        print("DONE ", filename)
        for date in dates:
            dates[date].close()
