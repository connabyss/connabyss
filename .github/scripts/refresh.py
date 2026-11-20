"""Refresh the parts of the profile that change on their own.

Each part lives between two markers, like <!-- auto:hof --> and <!-- /auto:hof -->.
Only the text between them is rewritten. If a source can't be read, that part is left as it was.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = "https://raw.githubusercontent.com/connabyss"


def fetch(url, token=False):
    req = urllib.request.Request(url, headers={"User-Agent": "profile-refresh"})
    if token and os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def numbered(text, heading):
    """The bold names of the numbered entries under one ## heading."""
    section = text.split(f"## {heading}", 1)[1]
    section = re.split(r"\n## ", section, maxsplit=1)[0]
    return [n.rstrip(".") for n in re.findall(r"^\d+\. \*\*(.+?)\*\*", section, re.M)]


def hall_of_fame(text):
    """Count the Finds and Breakers in HALL_OF_FAME.md and name the newest breaker."""
    finds, breakers = numbered(text, "Finds"), numbered(text, "Breakers")
    if not finds or not breakers:
        raise ValueError("no Finds or Breakers entries found")
    link = "https://github.com/connabyss/past-forever/blob/main/HALL_OF_FAME.md"
    return (f"The [Hall of Fame]({link}) has {len(finds)} finds, new lists found with it, "
            f"and {len(breakers)} breakers who caught it out. Newest breaker: **{breakers[-1]}**.")


def bite_version(data):
    v = json.loads(data)["info"]["version"]
    return f"[v{v} on PyPI](https://pypi.org/project/bite-check/)"


def sponsors(text):
    """Monthly sponsors listed in Bite's README go on this page too (the $10 tier promises it)."""
    m = re.search(r"^Monthly sponsors:(.*)$", text, re.M)
    if not m:
        raise ValueError("no 'Monthly sponsors:' line")
    names = m.group(1).strip()
    link = "https://github.com/sponsors/connabyss"
    if not names or "none yet" in names.lower():
        return f"Bite is free. [Sponsor it]({link}) for $10 a month and your name goes here."
    return f"Bite is kept going by {names.rstrip('.')}. Thank you. [Sponsor it]({link})."


def newest_merged(data, count=5):
    """The newest pull requests merged into other people's projects (not awesome-lists)."""
    lines = []
    items = sorted(json.loads(data)["items"], key=lambda i: i["closed_at"], reverse=True)
    for item in items:
        repo = item["repository_url"].split("/repos/", 1)[1]
        if "awesome" in repo.lower():
            continue
        title = re.sub(r"^\w+(\([^)]*\))?!?: ", "", item["title"])  # drop "fix(x): "
        title = title[:1].upper() + title[1:]
        lines.append(f"- **{repo.split('/')[1]}**: {title} ([#{item['number']}]({item['html_url']}))")
        if len(lines) == count:
            break
    if not lines:
        raise ValueError("no merged pull requests found")
    return "\n".join(lines)


def search_url():
    q = "author:connabyss is:pr is:merged -user:connabyss"
    return ("https://api.github.com/search/issues?"
            + urllib.parse.urlencode({"q": q, "sort": "updated", "order": "desc", "per_page": 50}))


PARTS = {
    "hof": ("README.md", lambda: hall_of_fame(fetch(f"{RAW}/past-forever/main/HALL_OF_FAME.md"))),
    "bite-version": ("README.md", lambda: bite_version(fetch("https://pypi.org/pypi/bite-check/json"))),
    "sponsors": ("README.md", lambda: sponsors(fetch(f"{RAW}/bite/main/README.md"))),
    "newest-merged": ("CONTRIBUTIONS.md", lambda: newest_merged(fetch(search_url(), token=True))),
}


def replace(text, name, body):
    pattern = re.compile(rf"(<!-- auto:{name} -->\n).*?(<!-- /auto:{name} -->)", re.S)
    if not pattern.search(text):
        raise ValueError(f"markers for {name} not found")
    return pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)


def main():
    failed = False
    for name, (file, make) in PARTS.items():
        path = ROOT / file
        try:
            body = make()
            text = path.read_text(encoding="utf-8")
            new = replace(text, name, body)
        except Exception as e:  # leave that part as it was
            print(f"{name}: skipped ({e})")
            failed = True
            continue
        if new != text:
            path.write_text(new, encoding="utf-8")
            print(f"{name}: updated")
        else:
            print(f"{name}: no change")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
