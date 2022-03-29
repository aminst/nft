from neo4j import GraphDatabase
import json

uri = "neo4j://10.8.0.2:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "root"))

def get_indegree(tx):
    nodes = []
    result = tx.run("MATCH(n) WITH n, size(()-[:TRANSFERED_TO]->(n)) as in_degree RETURN n, in_degree")

    for record in result:
        nodes.append(record['in_degree'])
    return nodes


def get_outdegree(tx):
    nodes = []
    result = tx.run("MATCH(n) WITH n, size((n)-[:TRANSFERED_TO]->()) as out_degree RETURN n, out_degree")

    for record in result:
        nodes.append(record['out_degree'])
    return nodes


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
    indegree = session.read_transaction(get_indegree)
    print("RECEIVED INDEGREE DATA")
    outdegree = session.read_transaction(get_outdegree)
    print("RECEIVED OUTDEGREE DATA")

    indegree_dict = list_to_dict(indegree)
    outdegree_dict = list_to_dict(outdegree)

    dict_to_file(indegree_dict, "indegree.json")
    dict_to_file(outdegree_dict, "outdegree.json")


driver.close()