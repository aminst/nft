CALL gds.degree.stream('nft_txs')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS name, score AS followers
ORDER BY followers DESC, name DESC