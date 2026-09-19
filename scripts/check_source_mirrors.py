#!/usr/bin/env python3
"""Fail CI when audited research/source pages drift apart.

The site copy under content/sources is intentionally a Hugo-shaped mirror of the
research note: `url` becomes `external_url` and the research-only H1 is omitted.
Everything else should stay identical.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "sources"
SITE = ROOT / "content" / "sources"
AUDITED_IDS = [f"SX-{i:03d}" for i in range(1, 9)]


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
    research_files = sorted(RESEARCH.glob("SX-*.md"))
    site_files = sorted(SITE.glob("sx-*.md"))
    errors = []

    if len(research_files) != 30:
        errors.append(f"research/sources: expected 30 notes, found {len(research_files)}")
    if len(site_files) != 30:
        errors.append(f"content/sources: expected 30 notes, found {len(site_files)}")

    for source_id in AUDITED_IDS:
        rpath = RESEARCH / f"{source_id}.md"
        spath = SITE / f"{source_id.lower()}.md"
        if not rpath.exists() or not spath.exists():
            errors.append(f"{source_id}: missing research or site copy")
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
        f"Source mirror check passed: 30/30 notes present; "
        f"{len(AUDITED_IDS)} audited pairs synchronized."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
