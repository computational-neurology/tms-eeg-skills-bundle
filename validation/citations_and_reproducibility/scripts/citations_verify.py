"""Exploratory: verify extracted citations against Crossref (existence of first-author+year; title/journal detail accuracy)."""
import difflib, json, time, unicodedata, urllib.parse, urllib.request
from pathlib import Path
import pandas as pd

CACHE = Path("analysis_extra/crossref_cache.json")
cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
TOPIC = "transcranial magnetic stimulation EEG"

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().strip()
    return s.split()[-1].split("-")[0] if s else ""

def crossref(params):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    if url not in cache:
        req = urllib.request.Request(url, headers={"User-Agent": "tmsval-citation-check/1.0"})
        for attempt in range(3):
            try:
                cache[url] = json.load(urllib.request.urlopen(req, timeout=30))["message"]["items"]; break
            except Exception as e:
                time.sleep(2 * (attempt + 1)); cache[url] = None
        CACHE.write_text(json.dumps(cache)); time.sleep(0.3)
    return cache[url] or []

def year_of(it):
    for k in ("published-print", "published-online", "issued"):
        dp = (it.get(k) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]: return dp[0][0]
    return None

def first_author(it):
    a = it.get("author") or []
    return norm(a[0].get("family", "")) if a else ""

def sim(a, b):
    return difflib.SequenceMatcher(None, (a or "").lower(), (b or "").lower()).ratio()

def find_author_year(key, year, hint):
    items = crossref({"query.author": key, "query.bibliographic": hint or TOPIC, "filter": f"from-pub-date:{year-1},until-pub-date:{year+1}", "rows": 40,
                      "select": "DOI,title,author,issued,published-print,published-online,container-title"})
    cands = [it for it in items if first_author(it) == key]
    exact = [it for it in cands if year_of(it) == year or (it.get("issued", {}).get("date-parts") or [[None]])[0][0] == year]
    best = (exact or cands or [None])[0]
    return ("exact" if exact else "pm1" if cands else "none"), best

if __name__ == "__main__":
    d = pd.read_csv("analysis_extra/citations_instances.csv", keep_default_na=False)
    # Level 1: existence of each unique first-author + year
    pairs = d.groupby(["key", "year"]).agg(surname=("surname", "first"), title=("title", lambda s: max(s, key=len)), n=("run_id", "size")).reset_index()
    res = []
    for p in pairs.itertuples():
        status, best = find_author_year(p.key, p.year, p.title if len(p.title) > 15 else "")
        if status == "none" and len(p.title) > 15:   # retry with topic query
            status, best = find_author_year(p.key, p.year, "")
        res.append(dict(key=p.key, year=p.year, surname=p.surname, n_instances=p.n, existence=status,
                        match_title=(best or {}).get("title", [""])[0] if best else "", match_year=year_of(best) if best else None,
                        match_doi=(best or {}).get("DOI", "") if best else ""))
    ex = pd.DataFrame(res); ex.to_csv("analysis_extra/citations_existence.csv", index=False)
    print(ex.existence.value_counts().to_dict())
    print(ex[ex.existence != "exact"].to_string(index=False))
    # Level 2: detail accuracy for reference-list entries with a title
    t = d[d.title.str.len() > 15].copy()
    out = []
    for r in t.itertuples():
        items = crossref({"query.bibliographic": r.title, "rows": 5, "select": "DOI,title,author,issued,published-print,published-online,container-title"})
        best = max(items, key=lambda it: sim(r.title, (it.get("title") or [""])[0]), default=None)
        s = sim(r.title, (best.get("title") or [""])[0]) if best else 0
        out.append(dict(run_id=r.run_id, arm=r.arm, cited=f"{r.surname} {r.year}", cited_title=r.title, cited_journal=r.journal,
                        title_found=s >= 0.75, title_similarity=round(s, 2),
                        real_first_author=first_author(best) if best else "", real_year=year_of(best) if best else None,
                        real_journal=((best or {}).get("container-title") or [""])[0] if best else "", real_doi=(best or {}).get("DOI", "") if best else ""))
    det = pd.DataFrame(out)
    det["author_ok"] = det.real_first_author == det.cited.str.split().str[0].map(norm)
    det["year_ok"] = (det.real_year - det.cited.str.split().str[-1].astype(int)).abs() <= 1
    det["journal_ok"] = [ (not cj) or (sim(cj, rj) > 0.6 or cj.lower() in rj.lower() or rj.lower() in cj.lower()) for cj, rj in zip(det.cited_journal, det.real_journal)]
    det["fully_correct"] = det.title_found & det.author_ok & det.year_ok & det.journal_ok
    det.to_csv("analysis_extra/citations_details.csv", index=False)
    print("\ndetail check:", len(det), "titled references")
    print(det.groupby("arm")[["title_found", "author_ok", "year_ok", "journal_ok", "fully_correct"]].mean().round(2))
    print(det[~det.fully_correct][["run_id", "arm", "cited", "cited_title", "title_similarity", "real_first_author", "real_year", "real_journal"]].to_string(index=False))
