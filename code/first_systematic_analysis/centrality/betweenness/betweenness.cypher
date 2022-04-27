CALL gds.betweenness.write('nft_txs', { writeProperty: 'betweenness_centrality' })
YIELD centralityDistribution, nodePropertiesWritten
RETURN centralityDistribution.min AS minimumScore, centralityDistribution.mean AS meanScore, nodePropertiesWritten