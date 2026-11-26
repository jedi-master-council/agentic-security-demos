"""Demo 21, current procedure: hosting concentration, version cadence and endpoint changes in a registry walk.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/registry_hosting.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "registry_hosting.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")

from collections import Counter
from urllib.parse import urlparse


def bump(a, b):
    x, y = [int(p) for p in a.split(".")], [int(p) for p in b.split(".")]
    return "major" if y[0] > x[0] else "minor" if y[1] > x[1] else "patch"


def registrable(host):
    return ".".join(host.split(".")[-2:])


def analyse(data):
    latest = {}
    for r in data["records"]:
        latest[r["server"]] = r
    hosts = Counter(urlparse(u).hostname for r in latest.values() for u in r["remotes"])
    n_end = sum(hosts.values())
    platform = sum(c for h, c in hosts.items() if any(h.endswith(s) for s in data["platform_suffixes"]))
    by = {}
    for r in data["records"]:
        by.setdefault(r["server"], []).append(r)
    trans, url_changes = [], []
    for s, rs in by.items():
        for a, b in zip(rs, rs[1:]):
            gap = b["published_h"] - a["published_h"]
            trans.append(gap)
            if a["remotes"] != b["remotes"]:
                ha = urlparse(a["remotes"][0]).hostname
                hb = urlparse(b["remotes"][0]).hostname
                url_changes.append({"server": s, "bump": bump(a["version"], b["version"]),
                                    "host_changed": ha != hb,
                                    "cross_domain": registrable(ha) != registrable(hb)})
    return {"endpoints": n_end, "hosts": dict(hosts), "top_host_share": round(max(hosts.values()) / n_end, 3),
            "platform_share": round(platform / n_end, 3), "transitions": len(trans),
            "within_24h": sum(g <= 24 for g in trans), "url_changes": url_changes,
            "secret_header_servers": sum(r["secret_header"] for r in latest.values()),
            "remote_servers": sum(bool(r["remotes"]) for r in latest.values())}


def main():
    a = analyse(load())
    print(f"latest-version endpoints {a['endpoints']} on {len(a['hosts'])} hosts; largest host share {a['top_host_share']:.2f}; under platform suffixes {a['platform_share']:.2f}")
    print(f"version transitions {a['transitions']}; within 24 hours of the previous version {a['within_24h']}")
    for c in a["url_changes"]:
        print(f"  endpoint change on {c['server']}: {c['bump']} bump; host changed {c['host_changed']}; across registrable domains {c['cross_domain']}")
    print(f"remote servers requiring a secret header {a['secret_header_servers']}/{a['remote_servers']}")
    print("lesson: the tool layer is hosted on few platforms and changes fast; an endpoint can move under a patch bump.")
    write("registry_hosting.json", dict(a, demo="demo-21-mcp-ecosystem"))


if __name__ == "__main__":
    main()
