# Verify the hash chain of a provision — the "don't trust us" example.
# Level 1 (this repo alone): recompute text_sha256 over text_md.
# Level 2 (with the evidence repo cloned alongside): verify the verbatim publisher
#   file's sha256 matches derived_from.sha256 — i.e. the clean text chains to the
#   exact bytes the state published.
# Run:  python examples/03_verify_hash_chain.py
import hashlib, json, pathlib, sys

vjson = pathlib.Path("lu-legilux/works/rgd-2023-07-21-a444/versions/2023-07-16/fr.json")
doc = json.loads(vjson.read_text(encoding="utf-8"))

ok = 0
for p in doc["provisions"]:
    got = hashlib.sha256(p["text_md"].encode("utf-8")).hexdigest()
    assert got == p["text_sha256"], f'MISMATCH at {p["provision_id"]}'
    ok += 1
print(f"level 1: {ok}/{len(doc['provisions'])} provision hashes recomputed OK")

src = doc["derived_from"]
evidence = pathlib.Path("..") / src["corpus_repo"] / src["path"]
if evidence.exists():
    got = hashlib.sha256(evidence.read_bytes()).hexdigest()
    assert got == src["sha256"], "MISMATCH between evidence file and derived_from.sha256"
    print(f"level 2: verbatim publisher file matches derived_from.sha256 ({got[:16]}...)")
    print(f"         source: {src['source_uri']}")
else:
    print(f"level 2 skipped: clone {src['corpus_repo']} next to this repo to verify "
          f"against the state-published bytes ({src['sha256'][:16]}...)")
