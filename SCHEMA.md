# lex-articles schema — `lex-articles/1`

This repository is the **consumption layer** of Lex: clean, per-provision,
point-in-time machine-readable law, deterministically derived from the verbatim
evidence repositories ([lex-corpus-lu-legilux](https://github.com/SFHAJJI/lex-corpus-lu-legilux),
[lex-corpus-eu-eurlex](https://github.com/SFHAJJI/lex-corpus-eu-eurlex)).
Every sentence here chains back to bytes the state published.

## Layout

```
catalog.json                                  # every work, both publishers
<publisher>/works/<slug>/
  work.json                                   # versions, languages, anchor inventory, relations
  history.json                                # per-anchor text states + anchor_events (the time axis)
  versions/<valid_from>/<lang>.md             # clean Markdown, YAML frontmatter
  versions/<valid_from>/<lang>.json           # structured provisions (this schema)
```

Versions whose source has no machine-readable manifestation upstream have no
directory here; they remain listed in the evidence repo with
`text.available:false`.

## IDs

Publisher-minted anchors are reused verbatim, never re-minted:

| Level | Example |
|---|---|
| Work | `lu-legilux:rgd-2023-07-21-a444` |
| Version | `lu-legilux:rgd-2023-07-21-a444:2023-07-16` |
| Provision (point-in-time) | `lu-legilux:rgd-2023-07-21-a444:2023-07-16#art_1er` |

`provision_id` is the foreign key downstream systems (obligation registers,
judgment layers) attach to. A renumbered article is a different provision;
renumbering is *detected and disclosed* (see `anchor_events`), never papered over.

## The hash chain

```
provision.text_sha256            sha256 over text_md (UTF-8, exactly as stored)
  -> derived_from.sha256         sha256 over the verbatim publisher file (evidence repo)
    -> observation chain         append-only, inside hashed records
      -> signed index stamp      ECDSA-P256
```

Verifying a single provision requires the whole source document **and** the
extractor at the pinned profile version: the claim is "profile P over document D
yields exactly this text", which is mechanically checkable offline.

## Extraction profiles are immutable and permanently retained

`akn-lu/1`, `xhtml-eu/1` and `fmx4-eu/1` will remain runnable for the life of
the project. A profile is never edited after publication; an improved extraction
is a **new** profile (`akn-lu/2`) beside the old one, and re-derivation under a
new profile is a new, tagged generation. Citations pinned under a profile verify
under that profile, forever. Every `*.json` records its profile in
`generator.profile`; `history.json` lists the profiles that produced it.

- **LU (`akn-lu/1`)** — structural: article boundaries, anchors, per-article
  ELIs and applicability dates are the publisher's own (Akoma Ntoso eIds +
  JOLUX metadata).
- **EU (`fmx4-eu/1`)** — structural: Formex 4 is the Publications Office's own
  production XML; `ARTICLE`/`PARAG` boundaries and numbering are publisher
  markup. Anchors continue the `xhtml-eu/1` convention (`art_N`, `anx_<roman>`)
  so permalinks and history states survive the profile switch. A work uses
  `fmx4-eu/1` only when every body-bearing version has a Formex manifestation;
  the evidence lives in the corpus repo under `versions/{date}/en.fmx4/`
  (verbatim zip members, one sha256 observation each).
- **EU fallback (`xhtml-eu/1`)** — structural-in-presentation: boundaries follow
  the publisher's `eli-subdivision` fragment identifiers in Cellar's
  consolidated XHTML (or its older flat format). Still used for works where a
  Formex manifestation is missing upstream for at least one version.

## Spans

`md_span` offsets are **Unicode scalar values** (codepoints), 0-based,
half-open `[start, end)`, into the sibling `.md` file (frontmatter included).
Slicing the Markdown by the span yields exactly `text_md`. This is asserted by
tests on every build.

## Validity: two truths, disclosed

- `article_valid_from` (provision level) is the **publisher-asserted** valid
  time (`dateApplicability`) — what a court cares about.
- `history.json` intervals are **observed text identity** — what the bytes say,
  grouped by `text_sha256` across versions.

Where they disagree, the state carries `validity_conflict: true`. Disagreement
is disclosed data, never silently resolved: a publisher whose article dates
contradict its own text is exactly what this corpus exists to surface.

## history.json

Per anchor: the distinct texts the provision has had, as validity intervals
(`valid_from`, `valid_to`, `text_sha256`, `in_version`). Per version
transition: `anchor_events` — `inserted`, `removed`, and `renumbered` (emitted
only when the text-hash match between one removed and one inserted anchor is
unique within the transition; identical boilerplate stays honest
removed/inserted).

## Provision object (one entry of `provisions[]`)

```json
{
  "anchor": "art_1er",
  "provision_id": "lu-legilux:rgd-2023-07-21-a444:2023-07-16#art_1er",
  "eli": "http://data.legilux.public.lu/eli/etat/leg/rgd/2023/07/21/a444/art_1er/20230716",
  "type": "article | annex",
  "num": "Art. 1er.",
  "heading": null,
  "path": ["Chapitre Ier — Objet"],
  "article_valid_from": "2023-07-16",
  "text_md": "…clean Markdown; amendment markers and hyperlinks are structured fields, never inline…",
  "text_sha256": "…",
  "md_span": { "start": 412, "end": 561 },
  "citations": [ { "href": "http://data.legilux.public.lu/eli/…", "text": "loi du 31 juillet 2006" } ]
}
```

## Licensing

- LU content: **CC-BY-4.0** (Legilux — Ministère d'État, Service central de
  législation). Attribution rides inside every file.
- EU content: reuse with attribution per **Commission Decision 2011/833/EU**;
  consolidated texts have no legal effect — only the Official Journal is
  authentic.
- This derived compilation: **CC-BY-4.0**.

Everything in this repository is regenerable: it is a pure function of
(evidence repos × pinned profile). Deleting it loses nothing but compute.
