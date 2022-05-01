CALL gds.eigenvector.write('txs', {
               maxIterations: 20,
               writeProperty: 'eigenvector_centrality'
             })
             YIELD nodePropertiesWritten, ranIterations;