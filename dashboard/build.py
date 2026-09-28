"""Gera dashboard/index.html a partir das exportações do Events Manager em data/raw/*.xlsx.

Uso: python3 dashboard/build.py   (requer pandas + openpyxl)
"""
import glob, json, pathlib
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
OTHER = ["facebook_sdk_received_count", "mmp_received_count", "ae_api_received_count", "ads_sdk_received_count"]

rows = {}
for f in sorted(glob.glob(str(ROOT / "data/raw/*.xlsx"))):
    d = pd.read_excel(f)
    d["t"] = pd.to_datetime(d["unix_time_start"], errors="coerce")
    d = d.dropna(subset=["t", "event"])
    for _, r in d.iterrows():
        t = r.t.strftime("%Y-%m-%dT%H")
        rows[(t, r.event)] = [t, r.event, int(r.browser_received_count), int(r.server_received_count),
                              int(sum(r[c] for c in OTHER)), int(r.total_count)]

data = json.dumps(sorted(rows.values()), separators=(",", ":"), ensure_ascii=False)
tpl = (ROOT / "dashboard/pixel-template.html").read_text()
(ROOT / "dashboard/index.html").write_text(tpl.replace("/*DATA*/", data))
print(f"{len(rows)} linhas -> dashboard/index.html")
