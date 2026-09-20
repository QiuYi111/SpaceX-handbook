#!/usr/bin/env python3
"""Validate the public source catalog against source-note front matter.

The site renders data/sources.json in the source index while individual notes
carry their own front matter. This guard prevents the two metadata surfaces from
silently disagreeing.
"""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "sources.json"
SITE_SOURCES = ROOT / "content" / "sources"
EXPECTED_IDS = [f"SX-{i:03d}" for i in range(1, 31)]
REQUIRED_FIELDS = {"id", "tier", "title", "author", "date", "url", "themes"}


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        return value[1:-1]
    return value


def front_matter(path: Path) -> dict[str, str]:
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
        meta[key.strip()] = scalar(value)
    return meta


def main() -> int:
    errors = []
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    if not isinstance(catalog, list):
        print("Source catalog check failed: data/sources.json must be a list")
        return 1

    if len(catalog) != 30:
        errors.append(f"catalog: expected 30 entries, found {len(catalog)}")

    ids = [item.get("id") for item in catalog if isinstance(item, dict)]
    if len(ids) != len(set(ids)):
        errors.append("catalog: duplicate source IDs")
    if ids != EXPECTED_IDS:
        errors.append("catalog: IDs must be exactly SX-001..SX-030 in order")

    for item in catalog:
        if not isinstance(item, dict):
            errors.append("catalog: every entry must be an object")
            continue

        source_id = item.get("id", "<missing-id>")
        missing = sorted(REQUIRED_FIELDS - set(item))
        if missing:
            errors.append(f"{source_id}: missing catalog fields: {', '.join(missing)}")
            continue

        empty = sorted(k for k in REQUIRED_FIELDS if not str(item.get(k, "")).strip())
        if empty:
            errors.append(f"{source_id}: empty catalog fields: {', '.join(empty)}")

        if str(item.get("date", "")).strip().lower() == "current":
            errors.append(f"{source_id}: floating date 'current' is not allowed")

        note_path = SITE_SOURCES / f"{str(source_id).lower()}.md"
        if not note_path.exists():
            errors.append(f"{source_id}: missing site source note")
            continue

        try:
            meta = front_matter(note_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        expected = {
            "id": str(item["id"]),
            "tier": str(item["tier"]),
            "title": str(item["title"]),
            "external_url": str(item["url"]),
        }
        for key, value in expected.items():
            if meta.get(key) != value:
                errors.append(
                    f"{source_id}: catalog/note mismatch for {key}: "
                    f"{value!r} != {meta.get(key)!r}"
                )

    if errors:
        print("Source catalog check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Source catalog check passed: 30 entries synchronized with source-note metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
