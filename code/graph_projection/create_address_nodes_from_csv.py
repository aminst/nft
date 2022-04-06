import sys
import os
import csv

TO_ADDRESS = 8

if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])
    
    addresses = set()

    for filename in filenames:
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            addresses.add(row[TO_ADDRESS])

        print("READ ", filename)

    print(len(addresses))

    f = open('address_nodes.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['addressId:ID'])
    for address in addresses:
        writer.writerow([address])
    f.close()