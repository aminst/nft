from neo4j import GraphDatabase
import json
from datetime import datetime

uri = "neo4j://10.8.0.2:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "root"))

DATE_INDEX = 9



def get_days_after_mint(tx):
    tokens = dict()
    result = tx.run("MATCH ()-[r:TRANSFERED_TO]->() RETURN r.value as value, r.block_timestamp as time")

    counter = 0
    for record in result:
        if record['value'] != 'null':
            counter += 1
            date = (datetime.today() - datetime.strptime(record['time'][:10], '%Y-%m-%d')).days
            if date in tokens:
                tokens[date] += int(record['value'])
            else:
                tokens[date] = int(record['value'])
    print(counter)
    return tokens


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
    tokens = session.read_transaction(get_days_after_mint)
    # print("RECEIVED INDEGREE DATA")
    # outdegree = session.read_transaction(get_outdegree)
    print("RECEIVED DATA")

    # indegree_dict = list_to_dict(indegree)
    # outdegree_dict = list_to_dict(outdegree)
    
    dict_to_file(tokens, "market_value.json")
    # dict_to_file(outdegree_dict, "outdegree.json")


driver.close()