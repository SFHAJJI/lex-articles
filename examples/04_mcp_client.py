# Talk to the hosted Lex MCP endpoint directly (no AI, no key, standard library only):
# the same 8 tools any MCP-capable model uses. Shows article_history — the time axis.
# Run:  python examples/04_mcp_client.py
import json, urllib.request

MCP = "https://law.soufien.lu/mcp"

def call(method, params=None, id=1):
    body = json.dumps({"jsonrpc": "2.0", "id": id, "method": method, "params": params or {}}).encode()
    req = urllib.request.Request(MCP, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def tool(name, arguments):
    out = call("tools/call", {"name": name, "arguments": arguments})
    return json.loads(out["result"]["content"][0]["text"])

print("tools:", [t["name"] for t in call("tools/list")["result"]["tools"]])

# 1. find a work at article granularity
hits = tool("search", {"query": "own funds requirements", "publisher": "eu-eurlex", "limit": 3})
hit = hits[0]["hits"][0]
print(f'\nsearch hit: {hit["provision_id"]}  ({hit.get("permalink")})')

# 2. the time axis of one article: every distinct text it has had
hist = tool("article_history", {"work": "eu-eurlex:32013r0575", "anchor": "art_92"})
print(f'\nCRR Article 92 has had {hist["distinct_texts"]} distinct text(s):')
for s in hist["states"]:
    print(f'  {s["valid_from"]} -> {s["valid_to"] or "open"}  sha={s["text_sha256"][:12]}  {s.get("permalink", "")}')

# 3. fetch exactly one article's text as of a date (never the whole code)
sel = tool("as_of", {"work": "eu-eurlex:32013r0575", "date": "2020-01-01",
                     "mode": "select", "anchors": "art_92"})
print("\nArticle 92 as of 2020-01-01, first 300 chars:")
print(sel["provisions"][0]["text"][:300])
