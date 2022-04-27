from neo4j import GraphDatabase
import json

uri = "neo4j://10.8.0.2:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "root"))

def get_degree_centrality(tx):
    nodes = dict()
    result = tx.run("MATCH(n) RETURN n.addressId as address, n.degree as centrality")

    for record in result:
        nodes[record['address']] = record['centrality']
    return nodes


def write_to_file(d, name):
    with open(name, 'w') as convert_file:
        convert_file.write(json.dumps(d))


with driver.session() as session:
    pagerank = session.read_transaction(get_degree_centrality)
    print("RECEIVED DATA")
    write_to_file(pagerank, "out.json")

driver.close()