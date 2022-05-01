CALL gds.graph.project(
    "txs",
    {
        Address: {properties: "addressId"}
    },
    "TRANSFERED_TO"
)
YIELD
  graphName AS graph,
  relationshipProjection AS knowsProjection,
  nodeCount AS nodes,
  relationshipCount AS rels
