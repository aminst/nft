CALL gds.beta.closeness.write('nft_txs', { writeProperty: 'closeness_centrality' })
YIELD centralityDistribution, nodePropertiesWritten
RETURN centralityDistribution.min AS minimumScore, centralityDistribution.mean AS meanScore, nodePropertiesWritten
