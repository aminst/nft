from neo4j import GraphDatabase
import json
from datetime import datetime
import os
import sys
import csv
uri = "neo4j://10.8.0.2:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "root"))

TIME_STAMP = 3
VALUE = 14
START = 5
END = 8

def get_dict():
    d = (datetime.today() - datetime.strptime("2017-06-01", '%Y-%m-%d')).days
    new_dict = dict()
    for i in range(0,d):
        new_dict[i] = 0

    return new_dict

indegree_dict = get_dict()
outdegree_dict = get_dict()
number_of_nodes = get_dict()



# def get_zero_indegree(tx):
    
#     zero_indegree = tx.run("MATCH ()-[r:TRANSFERED_TO]->(n) WHERE n.addressId = '0x0000000000000000000000000000000000000000' RETURN r.block_timestamp as time")

#     for record in zero_indegree:
#         date = (datetime.today() - datetime.strptime(record['time'][:10], '%Y-%m-%d')).days

#         for d in indecree_dict.keys():
#             if d >= date:
#                 indecree_dict[d] += 1

#     return indecree_dict

# def get_zero_outdegree(tx):
    
#     outdegree_dict = tx.run("MATCH ()-[r:TRANSFERED_TO]->(n) WHERE n.addressId = '0x0000000000000000000000000000000000000000' RETURN r.block_timestamp as time")

#     for record in outdegree_dict:
#         date = (datetime.today() - datetime.strptime(record['time'][:10], '%Y-%m-%d')).days

#         for d in outdegree_dict.keys():
#             if d >= date:
#                 outdegree_dict[d] += 1

#     return outdegree_dict

# def get_number_of_nodes():
#     filenames = os.listdir(sys.argv[1])
#     print(filenames)
#     for key in number_of_nodes.keys():
#         number_of_nodes[key] = set()
#     for filename in filenames:
#         reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
#         for row in reader:
#             date = (datetime.today() - datetime.strptime(row[TIME_STAMP][:10], '%Y-%m-%d')).days
                
#             for d in number_of_nodes.keys():
#                 if d >= date:
#                     number_of_nodes[d].add(row[START])
#                     number_of_nodes[d].add(row[END])

#         print("READ ", filename)

#     return number_of_nodes


def get_number_of_nodes():
    filenames = os.listdir(sys.argv[1])
    filenames.sort()
    print(filenames)
    for key in number_of_nodes.keys():
        number_of_nodes[key] = set()
    for filename in filenames:
        reader = csv.reader(open(sys.argv[1] + '/' + filename, 'r'))
        for row in reader:
            date = (datetime.today() - datetime.strptime(row[TIME_STAMP][:10], '%Y-%m-%d')).days
                
            for d in number_of_nodes.keys():
                if d <= date:
                    number_of_nodes[d].add(row[START])
                    number_of_nodes[d].add(row[END])

            if row[START] == '0x0000000000000000000000000000000000000000':
                for d in outdegree_dict.keys():
                    if d <= date:
                        outdegree_dict[d] += 1

            if row[END] == '0x0000000000000000000000000000000000000000':
                for d in indegree_dict.keys():
                    if d <= date:
                        indegree_dict[d] += 1

        print("READ ", filename)

    return number_of_nodes

def list_to_dict(l):
    result = dict()
    for element in l:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result


def dict_to_file(d, name):
    with open(name, 'w') as convert_file:
        convert_file.write(json.dumps(d))


with driver.session() as session:
    number_of_nodes = get_number_of_nodes()
    print("NODES")
    # indegree = session.read_transaction(get_zero_indegree)
    print("INDEGREE")
    # outdegree = session.read_transaction(get_zero_outdegree)
    print("OUTDEGREE")
    print("RECEIVED DATA")

    result = dict()
    for key in indegree_dict:
        if len(number_of_nodes[key]) != 0:
            result[key] = (outdegree_dict[key] - indegree_dict[key]) / len(number_of_nodes[key])
    dict_to_file(result, "average_tokens.json")

driver.close()
