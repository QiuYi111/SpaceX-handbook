#!/usr/bin/env python3
"""Fail CI when audited research/source pages drift apart.

The site copy under content/sources is intentionally a Hugo-shaped mirror of the
research note: `url` becomes `external_url` and the research-only H1 is omitted.
Everything else should stay identical.

The audited source set is read from data/sources.json so adding a source cannot
silently bypass mirror validation or require another hard-coded count update.
"""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "sources"
SITE = ROOT / "content" / "sources"
CATALOG = ROOT / "data" / "sources.json"


def split_note(path: Path, research: bool):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"{path}: missing YAML front matter")

    meta = {}
    for raw in parts[1].strip().splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"{path}: unsupported front-matter line: {raw!r}")
        key, value = raw.split(":", 1)
        key = key.strip()
        if research and key == "url":
            key = "external_url"
        meta[key] = value.strip()

    body = parts[2].strip()
    if research:
        body = re.sub(r"^# SX-\d{3}[^\n]*\n+", "", body, count=1).strip()
    return meta, body


def main() -> int:
    errors = []

    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        audited_ids = [item["id"] for item in catalog]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"Source mirror check failed: cannot read catalog ids: {exc}")
        return 1

    expected = set(audited_ids)
    research_files = sorted(RESEARCH.glob("SX-*.md"))
    site_files = sorted(SITE.glob("sx-*.md"))
    research_ids = {path.stem.upper() for path in research_files}
    site_ids = {path.stem.upper() for path in site_files}

    missing_research = sorted(expected - research_ids)
    extra_research = sorted(research_ids - expected)
    missing_site = sorted(expected - site_ids)
    extra_site = sorted(site_ids - expected)

    if missing_research:
        errors.append("research/sources missing: " + ", ".join(missing_research))
    if extra_research:
        errors.append("research/sources not in catalog: " + ", ".join(extra_research))
    if missing_site:
        errors.append("content/sources missing: " + ", ".join(missing_site))
    if extra_site:
        errors.append("content/sources not in catalog: " + ", ".join(extra_site))

    for source_id in audited_ids:
        rpath = RESEARCH / f"{source_id}.md"
        spath = SITE / f"{source_id.lower()}.md"
        if not rpath.exists() or not spath.exists():
            continue
        try:
            rmeta, rbody = split_note(rpath, research=True)
            smeta, sbody = split_note(spath, research=False)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if rmeta != smeta:
            keys = sorted(set(rmeta) | set(smeta))
            diff = [k for k in keys if rmeta.get(k) != smeta.get(k)]
            errors.append(f"{source_id}: front matter drift in {', '.join(diff)}")
        if rbody != sbody:
            errors.append(f"{source_id}: body drift between research and site copy")

    if errors:
        print("Source mirror check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Source mirror check passed: {len(audited_ids)}/{len(audited_ids)} notes present; "
        f"{len(audited_ids)} audited pairs synchronized."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
