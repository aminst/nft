import sys
import os
import csv

TOKEN_ADDRESS_INDEX = 9
TOKEN_ID_INDEX = 10


if __name__ == "__main__":
    filenames = os.listdir(sys.argv[1])

    nfts = set()

    for filename in filenames:
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            nfts.add(row[TOKEN_ADDRESS_INDEX] + ':' + row[TOKEN_ID_INDEX])
        print("READ ", filename)
    
    print(len(nfts))

    f = open('nft_nodes.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['nftId:ID'])
    for nft in nfts:
        writer.writerow([nft])
    f.close()