CALL gds.graph.project(
    "txs",
    {
        Address: {properties: "addressId"}
    },
    {
        TRANSFERED_TO: {properties: ["amount", "block_hash", "block_number", "block_timestamp", "contract_type", "log_index", "operator", "token_address", "token_id", "transaction_hash", "transaction_index", "transaction_type", "value", "verified"]}
    }
)
YIELD
  graphName AS graph,
  relationshipProjection AS knowsProjection,
  nodeCount AS nodes,
  relationshipCount AS rels