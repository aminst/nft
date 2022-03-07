import requests
import json
import pymongo
from calendar import monthrange
import sys

headers = {
    'authority': 'deep-index.moralis.io',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'x-api-key': 'r0AsFN7sQQWKI2iRjAo0YGK6wi2U0kdTT9SVtAVw8CQZYXLGmqw7ZwNgszhuCli6',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://admin.moralis.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://admin.moralis.io/',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'if-none-match': 'W/"50718-zcFSTEoBkNGXrYr1MPdesXRSr/k"',
}

def print_exception(ex):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)

def main():
    # python3 trans.py 2021 1 -> 1/1/2021 - 1/2/2021
    year = sys.argv[1]
    month = sys.argv[2]
    collection_name = year + '-' + month

    try:
        conn = pymongo.MongoClient()
        print("Connected to DB")
    except:
        print("Could not connect to DB")
    
    db = conn.nft_transactions
    nft = db[collection_name]
    cursor = ''

    number_of_records = 0
    total = 1

    while number_of_records < total:
        try:
            from_date = month + '/' + "1" + '/' + year
            to_date = month + '/' + str(monthrange(int(year), int(month))[1]) + '/' + year
            params = (
                ('chain', 'eth'),
                ('from_date', from_date),
                ('to_date', to_date),
                ('format', 'hex'),
                ('cursor', cursor),
            )
            response = requests.get('https://deep-index.moralis.io/api/v2/nft/transfers', headers=headers, params=params)
            json_response = json.loads(response.content)

            cursor = json_response['cursor']
            print("NUMBER OF DATA: ", json_response['total'])
            total = json_response['total']
            number_of_records += int(json_response['page_size'])
            print("NUMBER OF RECORDS: ", number_of_records)
            print("CURSOR: ", cursor)

            transactions = json_response['result']
            for t in transactions:
                try:
                    nft.insert_one(t)
                except Exception as ex:
                    print_exception(ex)
        except Exception as ex:
            print_exception(ex)


if __name__ == "__main__":
    main()