# Stream the flat dataset (one JSON line per provision-version) straight from the
# release asset — the zero-clone path for data work. Standard library only.
# Run:  python examples/05_dataset_rows.py
import gzip, json, urllib.request

URL = ("https://github.com/SFHAJJI/lex-articles/releases/latest/download/"
       "eu-eurlex-provisions.jsonl.gz")   # 4 MB; the LU file is ~93 MB, same shape

with urllib.request.urlopen(URL, timeout=120) as r:
    rows = [json.loads(line) for line in gzip.open(r, "rt", encoding="utf-8")]

print(f"{len(rows)} provision rows")
# point-in-time filter in three lines: GDPR provisions valid on 2019-03-15
gdpr = [x for x in rows
        if x["lex_id"].startswith("eu-eurlex:32016r0679")
        and x["valid_from"] <= "2019-03-15" and (x["valid_to"] is None or x["valid_to"] >= "2019-03-15")]
print(f"GDPR provisions valid on 2019-03-15: {len(gdpr)}")
art33 = next(x for x in gdpr if x["anchor"] == "art_33")
print(f'\n{art33["provision_id"]}  ({art33["license"]})')
print(art33["text_md"][:300])
