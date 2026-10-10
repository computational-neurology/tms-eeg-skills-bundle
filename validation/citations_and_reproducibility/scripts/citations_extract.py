"""Exploratory: extract author-year citations from the 84 answers (post-hoc analysis, not pre-registered)."""
import re, unicodedata
import pandas as pd

SUR = r"(?:(?:van der|van|von|de|ter|da|di|le|la) )?[A-Z][A-Za-zÀ-ÿ'’\-]+"
YEAR = r"(?P<year>(?:19|20)\d{2})[a-z]?(?:/\d{2,4})?"
INTEXT = re.compile(rf"(?P<sur>{SUR})(?: (?:[A-Z]\.?){{1,3}})?(?P<etal> et al\.?| (?:and|&) {SUR})?,? \(?{YEAR}\)?")
STOP = {"In", "Since", "From", "Until", "By", "Before", "After", "Figure", "Table", "Version", "January", "February", "March", "April",
        "May", "June", "July", "August", "September", "October", "November", "December", "The", "See", "Also", "Updated", "Published", "Note"}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return s.split()[-1].split("-")[0] if s else s

REFLINE = re.compile(rf"^\s*(?:[-*]|\d+\.)\s+(?P<sur>{SUR}),?\s+(?:[A-Z][a-z]?\.?\s?-?)+.*?\({YEAR}\)\.?\s*(?P<title>[^*]*?)\.?\s*(?:\*(?P<journal>[^*]+)\*|$)")

def extract(text):
    out = []
    for line in text.splitlines():
        r = REFLINE.match(line)
        if r and r.group("sur").split()[-1] not in STOP:
            out.append(dict(surname=r.group("sur"), key=norm(r.group("sur")), year=int(r.group("year")), raw=line.strip()[:120],
                            in_reference_list=True, title=r.group("title").strip(" ."), journal=(r.group("journal") or "").strip(" .")))
            continue
        is_ref = bool(re.match(r"\s*(?:[-*]|\d+\.)\s+[A-Z][^\s]+ .*\(?(19|20)\d{2}", line)) and ("*" in line or "." in line[20:])
        for m in INTEXT.finditer(line):
            sur = m.group("sur")
            if sur.split()[-1] in STOP: continue
            before = line[max(0, m.start() - 1):m.start()]
            if not (m.group("etal") or before in ("(", ";", " ") and "(" in line[max(0, m.start() - 3):m.start()] or is_ref and m.start() < 12):
                continue
            title = ""
            if is_ref and m.start() < 12:
                rest = line[m.end():].strip(" .)")
                title = re.split(r"\*", rest)[0].strip(" .")
            out.append(dict(surname=sur, key=norm(sur), year=int(m.group("year")), raw=m.group(0).strip(), in_reference_list=bool(title), title=title,
                            journal=(re.findall(r"\*([^*]+)\*", line) or [""])[0] if title else ""))
    return out

if __name__ == "__main__":
    log = pd.read_csv("runs_log.csv", dtype=str, keep_default_na=False)
    rows = [dict(run_id=r.run_id, prompt_id=r.prompt_id, arm=r.arm, **c) for r in log.itertuples() for c in extract(open(f"runs/{r.run_id}.md").read())]
    d = pd.DataFrame(rows)
    d.to_csv("analysis_extra/citations_instances.csv", index=False)
    print(len(d), "citation instances;", d.groupby("arm").size().to_dict(), "| unique (author,year):", d[["key", "year"]].drop_duplicates().shape[0])
    print(d.groupby(["key", "year"]).size().sort_values(ascending=False).head(15).to_string())
    print(d.sample(12, random_state=1)[["run_id", "arm", "raw", "title"]].to_string())
