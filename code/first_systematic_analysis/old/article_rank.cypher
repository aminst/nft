CALL gds.articleRank.stream("nft_txs")
YIELD nodeId, score
WITH gds.util.asNode(nodeId) AS node, score
ORDER BY score DESC
LIMIT 5
RETURN node.addressId as addressId,
      score,
      size(()-[:TRANSFERED_TO]->(node)) as boughtCount,
      size((node)-[:TRANSFERED_TO]->()) as soldCount