# Examples — standard library only, no pip installs

Run from the repository root (`python examples/01_load_provisions.py`).

| file | shows |
|---|---|
| `01_load_provisions.py` | load one law/version; iterate clean per-article JSON |
| `02_point_in_time.py` | "what did this law say on date D?" from the files alone — including the honest refusals (`no_version_for_date`, `anchor_not_in_version`) |
| `03_verify_hash_chain.py` | recompute every article hash; with the evidence repo cloned alongside, verify against the exact state-published bytes |
| `04_mcp_client.py` | the hosted MCP endpoint raw (no AI, no key): search → `article_history` time axis → `as_of mode=select` for one article |
| `05_dataset_rows.py` | stream the flat JSONL release asset and do a point-in-time filter in three lines |

Building a RAG/agent? The provisions **are** the chunks: embed `text_md`, key by
`provision_id`, filter `valid_from`/`valid_to` **before** similarity, and always
carry `permalink` + `text_sha256` into your citations so answers stay auditable.
