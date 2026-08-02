# Point-in-time resolution from the files alone: "what did this law say on date D?"
# The version directories are named by valid_from; valid_to is in each json.
# Run:  python examples/02_point_in_time.py lu-legilux/works/rgd-1998-08-03-n4 2018-01-01 art_1er
import json, pathlib, sys

work_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "lu-legilux/works/rgd-1998-08-03-n4")
date = sys.argv[2] if len(sys.argv) > 2 else "2018-01-01"
anchor = sys.argv[3] if len(sys.argv) > 3 else "art_1er"

# pick the version whose [valid_from, valid_to] interval contains the date
best = None
for vdir in sorted((work_dir / "versions").iterdir()):
    if vdir.name[:10] <= date:
        best = vdir
if best is None:
    sys.exit(f"honest refusal: no version of {work_dir.name} was valid on {date} (no_version_for_date)")

doc = json.loads(next(best.glob("*.json")).read_text(encoding="utf-8"))
if doc["valid_to"] and doc["valid_to"] < date:
    sys.exit(f"honest refusal: latest version before {date} expired {doc['valid_to']} (no_version_for_date)")

prov = next((p for p in doc["provisions"] if p["anchor"] == anchor), None)
if prov is None:
    sys.exit(f"honest refusal: {anchor} did not exist in the version valid on {date} (anchor_not_in_version)")

print(f'{doc["lex_id"]}  (valid {doc["valid_from"]} -> {doc["valid_to"] or "open"})')
print(f'{prov["num"] or prov["anchor"]}  sha256={prov["text_sha256"][:16]}...')
print("-" * 72)
print(prov["text_md"])
