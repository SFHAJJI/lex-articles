# lex-articles

[![License](https://img.shields.io/badge/license-CC--BY--4.0-blue?style=flat-square)](LICENSE)
[![Live](https://img.shields.io/badge/live-law.soufien.lu-e0705f?style=flat-square)](https://law.soufien.lu)
[![Records](https://img.shields.io/badge/dataset-live%20catalog-brightgreen?style=flat-square)](catalog.json)
[![Formats](https://img.shields.io/badge/formats-JSON%20%C2%B7%20JSONL%20%C2%B7%20parquet-orange?style=flat-square)](README.md)
[![Engine](https://img.shields.io/badge/engine-SFHAJJI%2Flex-24292f?style=flat-square)](https://github.com/SFHAJJI/lex)

**Machine-readable Luxembourg + EU law, per article, point-in-time, verifiable.**
Clean Markdown and structured JSON for every provision of every consolidated
version, with validity dates, stable publisher-minted IDs, and a hash chain
back to the exact bytes the state published.

The generated [catalog](catalog.json) and release assets are the source of truth
for work, version, provision, and distinct-text counts. They are regenerated
from the evidence repositories rather than copied into prose.

- **Luxembourg**, every machine-readable version in Legilux's consolidated
  collection. Versions without usable official text keep their dates and source
  link rather than being dropped or reconstructed.
- **EU**, the reviewed, configuration-led scope in French and English, including
  every available original and consolidated expression and the legal
  relationships needed for temporal tracing. When an amended work has no
  official consolidation, its record and amendment timeline remain available
  with `consolidation_status=not_published`; Lex never manufactures merged text.

**[Examples](examples/)** ·
**[Schema contract](SCHEMA.md)** ·
**[Releases (JSONL + parquet)](https://github.com/SFHAJJI/lex-articles/releases)** ·
**[Live demo](https://law.soufien.lu)** ·
**[MCP endpoint](https://law.soufien.lu/mcp)** ·
**[Engine](https://github.com/SFHAJJI/lex)**

## Use it with AI in 60 seconds

Every provision is one clean row: point-in-time RAG without writing a parser.

```python
import json, pathlib
doc = json.loads(pathlib.Path(
    "lu-legilux/works/rgd-2023-07-21-a444/versions/2023-07-16/fr.json").read_text(encoding="utf-8"))
for p in doc["provisions"]:
    print(p["provision_id"], p["article_valid_from"], p["text_md"][:80])
```

Or skip cloning entirely, one flat file, one row per provision-version
([release assets](https://github.com/SFHAJJI/lex-articles/releases), licence
inline in every row, JSONL.gz and parquet):

```sql
-- DuckDB, zero install beyond duckdb itself
SELECT anchor, valid_from, valid_to, text_md
FROM read_parquet('https://github.com/SFHAJJI/lex-articles/releases/latest/download/lu-legilux-provisions.parquet')
WHERE lex_id LIKE 'lu-legilux:rgd-2023-07-21-a444%'
  AND valid_from <= '2023-08-01' AND (valid_to IS NULL OR valid_to >= '2023-08-01');
```

Or talk to the same data through the hosted MCP endpoint (any MCP client, no
key). The read-only tools cover both Luxembourg and EU material, including
search, per-article `as_of`, timelines, history, comparison, and provenance:

```
claude mcp add --transport http lex https://law.soufien.lu/mcp
```

Five runnable, dependency-free scripts live in [examples/](examples/), load,
point-in-time resolution with honest refusals, hash-chain verification, a raw
MCP client, and dataset streaming.

## What a question about time looks like

*"What has Article 2 of this regulation said over its life?"* is a file read,
not a computation, `history.json` holds every distinct text a provision has
had, as validity intervals:

```json
"art_2": [
  { "valid_from": "2023-07-16", "valid_to": "2023-10-25", "text_sha256": "aaa…", "in_version": "…:2023-07-16" },
  { "valid_from": "2023-10-26", "valid_to": null,          "text_sha256": "bbb…", "in_version": "…:2023-10-26" }
]
```

`anchor_events` additionally reports insertions, removals, and mechanically
detected renumberings ("art_5 became art_5bis on 2023-10-26, identical text"), the signal that keeps an obligation register attached to the right provision.

## Why you can trust it (collection & processing)

This repo is the **consumption layer**. The **evidence layer**, [lex-corpus-lu-legilux](https://github.com/SFHAJJI/lex-corpus-lu-legilux) and
[lex-corpus-eu-eurlex](https://github.com/SFHAJJI/lex-corpus-eu-eurlex), holds
the verbatim files the publishers serve (Akoma Ntoso XML for Luxembourg,
Formex 4 / XHTML for the EU), sha256-hashed, append-only, fetched only from
official robots-permitted channels. Every `text_sha256` here chains to a
verbatim-file hash there; extraction is deterministic, versioned,
immutable-per-profile code (never an LLM). Re-run the pinned open-source
extractor on the state's bytes and you get these bytes, `examples/03_verify_hash_chain.py` does it in 25 lines. See
[SCHEMA.md](SCHEMA.md) for the full contract (IDs, spans, profiles, validity
semantics).

## Maintenance

Regenerated **nightly** when the law changes, by the same pipeline that serves
[law.soufien.lu](https://law.soufien.lu). A determinism guard blocks any commit
where derived files changed without a corpus change (extractor drift can never
masquerade as legislation). HEAD is the contract; release assets are rebuilt on
change.

## Layout

```
catalog.json                                   # every work, both publishers
<publisher>/works/<slug>/
  work.json        # versions, languages, anchors, relations (reserved)
  history.json     # per-anchor text states + anchor_events, the time axis
  versions/<valid_from>/fr.md                  # clean Markdown, frontmatter
  versions/<valid_from>/fr.json                # structured provisions
```

## Contributing & citing

Gaps, mis-extractions, or a jurisdiction you want covered, open an issue.
Extraction improvements ship as **new** profiles beside the old (published
profiles are immutable, so pinned citations verify forever). If you use this
dataset in research or a product, cite it as *"Lex, point-in-time Luxembourg
and EU law (github.com/SFHAJJI/lex-articles)"* and keep the per-row publisher
attribution.

## Licence & attribution

Derived compilation: **CC-BY-4.0**. Luxembourg content: **CC-BY-4.0**
(Legilux, Ministère d'État, Service central de législation). EU content:
reuse with attribution per Commission Decision 2011/833/EU; **consolidated
texts have no legal effect**, only the Journal officiel / Official Journal is
authentic. Attribution rides inside every file. Lex states what the rule *was*;
it never interprets.

Built nightly by [lex](https://github.com/SFHAJJI/lex) · browse and time-travel
at [law.soufien.lu](https://law.soufien.lu)

## Support

This is free and open, and it stays that way whatever you decide. It is also not free to run:
the live site, the nightly jobs and the storage sit on Azure infrastructure I pay for out of
pocket, and I maintain it on my own time.

If it saved you an afternoon, you can [buy me a coffee ☕](https://buymeacoffee.com/shajji)
and put it towards the hosting bill. Starring the repo helps just as much, and costs nothing.
