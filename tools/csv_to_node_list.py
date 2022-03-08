import sys
import os
import csv

FROM_ADDRESS = 6
TO_ADDRESS = 9

if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])
    
    addresses = set()

    for filename in filenames:
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        next(reader)
        for row in reader:
            addresses.add(row[FROM_ADDRESS])
            addresses.add(row[TO_ADDRESS])

        print("READ ", filename)

    print(len(addresses))

    f = open('nodes.csv', 'w')
    writer = csv.writer(f)
    for address in addresses:
        writer.writerow(address)
    f.close()