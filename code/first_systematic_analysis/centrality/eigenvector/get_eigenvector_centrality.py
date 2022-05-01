from neo4j import GraphDatabase
import json

uri = "neo4j://10.8.0.2:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "root"))

def get_eigenvector_centrality(tx):
    nodes = dict()
    result = tx.run("MATCH(n) RETURN n.addressId as address, n.eigenvector_centrality as eigenvector")

    for record in result:
        nodes[record['address']] = record['eigenvector']
    return nodes


def write_to_file(d, name):
    with open(name, 'w') as convert_file:
        convert_file.write(json.dumps(d))


with driver.session() as session:
    eigenvector = session.read_transaction(get_eigenvector_centrality)
    print("RECEIVED DATA")
    write_to_file(eigenvector, "eigenvector.json")

driver.close()