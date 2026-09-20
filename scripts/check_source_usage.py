#!/usr/bin/env python3
"""Keep handbook source declarations and inline citations synchronized.

Each handbook chapter has a source_ids front-matter list used by the site UI.
Every declared source must be cited in the chapter body, and every source
shortcode used in the body must be declared. This prevents "bibliography by
association" and keeps important claims tied to nearby evidence.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "content" / "handbook"
SOURCES = ROOT / "content" / "sources"

SOURCE_ID_RE = re.compile(r"SX-\d{3}")
SHORTCODE_RE = re.compile(r'\{\{<\s*source\s+"(SX-\d{3})"\s*>\}\}')
DECL_RE = re.compile(r"source_ids:\s*\[([^\]]*)\]")


def main() -> int:
    known = {path.stem.upper() for path in SOURCES.glob("sx-*.md")}
    errors = []
    chapters = 0
    citations = 0

    for path in sorted(HANDBOOK.glob("*.md")):
        if path.name == "_index.md":
            continue
        chapters += 1
        text = path.read_text(encoding="utf-8")

        frontmatter = text.split("---", 2)
        if len(frontmatter) != 3:
            errors.append(f"{path}: missing YAML front matter")
            continue

        match = DECL_RE.search(frontmatter[1])
        declared = SOURCE_ID_RE.findall(match.group(1)) if match else []
        cited = SHORTCODE_RE.findall(frontmatter[2])
        citations += len(cited)

        if len(declared) != len(set(declared)):
            errors.append(f"{path}: duplicate source_ids")
        unknown = sorted((set(declared) | set(cited)) - known)
        if unknown:
            errors.append(f"{path}: unknown source ids: {', '.join(unknown)}")

        unused = sorted(set(declared) - set(cited))
        undeclared = sorted(set(cited) - set(declared))
        if unused:
            errors.append(
                f"{path}: declared but not cited in body: {', '.join(unused)}"
            )
        if undeclared:
            errors.append(
                f"{path}: cited but missing from source_ids: {', '.join(undeclared)}"
            )

    if errors:
        print("Chapter source usage check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Chapter source usage check passed: {chapters} chapters, "
        f"{citations} inline source citations."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
