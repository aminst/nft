CALL gds.louvain.write('txs', { writeProperty: 'community' })
YIELD communityCount, modularity, modularities