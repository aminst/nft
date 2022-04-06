import sys
import os
import csv

TO_ADDRESS = 8
TOKEN_ADDRESS_INDEX = 9
TOKEN_ID_INDEX = 10


if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])

    f = open('relationship.csv', 'w')
    writer = csv.writer(f)
    writer.writerow([':START_ID', ':END_ID'])

    for filename in filenames:
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            writer.writerow([row[TO_ADDRESS], row[TOKEN_ADDRESS_INDEX] + ':' + row[TOKEN_ID_INDEX]])

        print("READ ", filename)
    
    f.close()