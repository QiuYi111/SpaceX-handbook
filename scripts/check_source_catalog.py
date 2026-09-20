#!/usr/bin/env python3
"""Validate the public source catalog against source-note front matter.

The site keeps source metadata in two places:
- data/sources.json drives citation/source-list rendering;
- content/sources/sx-*.md stores research notes and their external_url.

This guard prevents metadata drift, malformed catalog entries, non-contiguous
source IDs, and floating source dates from silently reaching citations or the
source index.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "sources.json"
NOTES = ROOT / "content" / "sources"
SOURCE_INDEX = NOTES / "_index.md"

ID_RE = re.compile(r"^SX-\d{3}$")
COUNT_RE = re.compile(r"收录目前使用的 \*\*(\d+) 个主要来源\*\*")
REQUIRED_FIELDS = {"id", "tier", "title", "author", "date", "url", "themes"}
ALLOWED_TIERS = {
    "P0",
    "P0*",
    "P1",
    "P1V",
    "P1-support",
    "P1-transfer",
    "P1/P2",
    "P2",
    "P2+",
    "P3",
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("missing YAML front matter")

    values: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key.strip()] = value
    return values


def main() -> int:
    errors: list[str] = []

    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Source catalog check failed: cannot read {CATALOG}: {exc}")
        return 1

    if not isinstance(catalog, list):
        print("Source catalog check failed: data/sources.json must contain a list")
        return 1
    if not catalog:
        print("Source catalog check failed: data/sources.json must not be empty")
        return 1

    ids = [item.get("id") for item in catalog if isinstance(item, dict)]
    if len(ids) != len(set(ids)):
        errors.append("data/sources.json contains duplicate source ids")
    expected_ids = [f"SX-{i:03d}" for i in range(1, len(catalog) + 1)]
    if ids != expected_ids:
        errors.append(
            f"catalog IDs must be contiguous SX-001..SX-{len(catalog):03d} in order"
        )

    known: dict[str, dict[str, str]] = {}
    for index, item in enumerate(catalog, start=1):
        if not isinstance(item, dict):
            errors.append(f"catalog item #{index} is not an object")
            continue

        source_id = item.get("id", "")
        missing = sorted(REQUIRED_FIELDS - set(item))
        if missing:
            errors.append(f"{source_id or f'item #{index}'}: missing fields: {', '.join(missing)}")
            continue

        empty = sorted(k for k in REQUIRED_FIELDS if not str(item.get(k, "")).strip())
        if empty:
            errors.append(f"{source_id}: empty fields: {', '.join(empty)}")

        tier = item.get("tier", "")
        url = item.get("url", "")
        date = str(item.get("date", "")).strip()

        if not ID_RE.fullmatch(source_id):
            errors.append(f"catalog item #{index}: invalid id {source_id!r}")
            continue
        if tier not in ALLOWED_TIERS:
            errors.append(f"{source_id}: unsupported tier {tier!r}")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{source_id}: url must be an https URL")
        if date.lower() == "current":
            errors.append(f"{source_id}: floating date 'current' is not allowed")

        known[source_id] = item

    note_paths = {path.stem.upper(): path for path in NOTES.glob("sx-*.md")}
    missing_notes = sorted(set(known) - set(note_paths))
    extra_notes = sorted(set(note_paths) - set(known))
    if missing_notes:
        errors.append("catalog entries missing source notes: " + ", ".join(missing_notes))
    if extra_notes:
        errors.append("source notes missing catalog entries: " + ", ".join(extra_notes))

    for source_id in sorted(set(known) & set(note_paths)):
        path = note_paths[source_id]
        try:
            meta = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue

        expected = known[source_id]
        comparisons = {
            "id": expected.get("id", ""),
            "tier": expected.get("tier", ""),
            "title": expected.get("title", ""),
            "external_url": expected.get("url", ""),
        }
        for field, expected_value in comparisons.items():
            actual = meta.get(field, "")
            if actual != expected_value:
                errors.append(
                    f"{path}: {field} mismatch: note={actual!r}, catalog={expected_value!r}"
                )

        if not meta.get("access"):
            errors.append(f"{path}: missing access field")

    try:
        index_text = SOURCE_INDEX.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read {SOURCE_INDEX}: {exc}")
    else:
        match = COUNT_RE.search(index_text)
        if match and int(match.group(1)) != len(catalog):
            errors.append(
                f"{SOURCE_INDEX}: says {match.group(1)} sources, catalog has {len(catalog)}"
            )

    if errors:
        print("Source catalog check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Source catalog check passed: {len(catalog)} catalog entries and "
        f"{len(note_paths)} source notes are synchronized."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
