# Load one law, one version, per article — no dependencies beyond the standard library.
# Run from the repo root:  python examples/01_load_provisions.py
import json, pathlib

doc = json.loads(pathlib.Path(
    "lu-legilux/works/rgd-2023-07-21-a444/versions/2023-07-16/fr.json"
).read_text(encoding="utf-8"))

print(doc["title"])
print(f'valid {doc["valid_from"]} -> {doc["valid_to"] or "open"}   '
      f'profile {doc["generator"]["profile"]}   licence {doc["license"]}')
print("-" * 72)
for p in doc["provisions"]:
    label = p["num"] or p["heading"] or p["anchor"]
    print(f'{p["provision_id"]}')
    print(f'  {label}: {p["text_md"][:100]}...')
