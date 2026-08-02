# lex-articles

**Machine-readable Luxembourg + EU law, per article, point-in-time, verifiable.**
Clean Markdown and structured JSON for every provision of every consolidated
version — with validity dates, stable publisher-minted IDs, and a hash chain
back to the exact bytes the state published.

**1,212 works · 2,912 derived versions · 88,815 provisions · 102,371 distinct
text states** (Luxembourg: full consolidated corpus, 1849→2030 · EU: GDPR,
DORA, AI Act, NIS2, MiFID II, CRR, PSD2, SFDR).

## Use it with AI in 60 seconds

Every provision is one clean row: point-in-time RAG without writing a parser.

```python
import json, pathlib
doc = json.loads(pathlib.Path(
    "lu-legilux/works/rgd-2023-07-21-a444/versions/2023-07-16/fr.json").read_text(encoding="utf-8"))
for p in doc["provisions"]:
    print(p["provision_id"], p["article_valid_from"], p["text_md"][:80])
```

Or skip cloning entirely — one flat file, one line per provision-version
([release assets](https://github.com/SFHAJJI/lex-articles/releases), licence
inline in every row):

```sql
-- DuckDB, zero install beyond duckdb itself
SELECT anchor, valid_from, valid_to, text_md
FROM read_json_auto('https://github.com/SFHAJJI/lex-articles/releases/latest/download/lu-legilux-provisions.jsonl.gz')
WHERE lex_id LIKE 'lu-legilux:rgd-2023-07-21-a444%'
  AND valid_from <= '2023-08-01' AND (valid_to IS NULL OR valid_to >= '2023-08-01');
```

Or talk to the same data through the hosted MCP endpoint (any MCP client, no
key) — 8 tools including per-article `as_of` (outline/select modes) and
`article_history`:

```
claude mcp add --transport http lex https://law.soufien.lu/mcp
```

## What a question about time looks like

*"What has Article 2 of this regulation said over its life?"* is a file read,
not a computation — `history.json` holds every distinct text a provision has
had, as validity intervals:

```json
"art_2": [
  { "valid_from": "2023-07-16", "valid_to": "2023-10-25", "text_sha256": "aaa…", "in_version": "…:2023-07-16" },
  { "valid_from": "2023-10-26", "valid_to": null,          "text_sha256": "bbb…", "in_version": "…:2023-10-26" }
]
```

`anchor_events` additionally reports insertions, removals, and mechanically
detected renumberings ("art_5 became art_5bis on 2023-10-26, identical text") —
the signal that keeps an obligation register attached to the right provision.

## Why you can trust it

This repo is the **consumption layer**. The **evidence layer** —
[lex-corpus-lu-legilux](https://github.com/SFHAJJI/lex-corpus-lu-legilux) and
[lex-corpus-eu-eurlex](https://github.com/SFHAJJI/lex-corpus-eu-eurlex) — holds
the verbatim files the publishers serve, sha256-hashed, append-only. Every
`text_sha256` here chains to a verbatim-file hash there; extraction is
deterministic, versioned, immutable-per-profile code (never an LLM). Re-run the
pinned open-source extractor on the state's bytes and you get these bytes.
See [SCHEMA.md](SCHEMA.md) for the full contract (IDs, spans, profiles,
validity semantics).

## Layout

```
catalog.json                                   # every work, both publishers
<publisher>/works/<slug>/
  work.json        # versions, languages, anchors, relations (reserved)
  history.json     # per-anchor text states + anchor_events — the time axis
  versions/<valid_from>/fr.md                  # clean Markdown, frontmatter
  versions/<valid_from>/fr.json                # structured provisions
```

## Licence & attribution

Derived compilation: **CC-BY-4.0**. Luxembourg content: **CC-BY-4.0**
(Legilux — Ministère d'État, Service central de législation). EU content:
reuse with attribution per Commission Decision 2011/833/EU; **consolidated
texts have no legal effect** — only the Journal officiel / Official Journal is
authentic. Attribution rides inside every file. Lex states what the rule *was*;
it never interprets.

Built nightly by [lex](https://github.com/SFHAJJI/lex) · browse and time-travel
at [law.soufien.lu](https://law.soufien.lu)
