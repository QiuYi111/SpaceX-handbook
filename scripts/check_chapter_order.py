#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path("content/handbook")
errors = []
rows = []

for path in sorted(root.glob("[0-9][0-9]-*.md")):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(?m)^weight:\s*(\d+)\s*$", text)
    if not m:
        errors.append(f"{path}: missing numeric weight")
        continue
    prefix = int(path.name[:2])
    weight = int(m.group(1))
    rows.append((prefix, weight, path.name))

for (p1, w1, n1), (p2, w2, n2) in zip(rows, rows[1:]):
    if p2 <= p1:
        errors.append(f"filename order: {n1} -> {n2}")
    if w2 <= w1:
        errors.append(f"weight order: {n1} ({w1}) -> {n2} ({w2})")

weights = [w for _, w, _ in rows]
if len(weights) != len(set(weights)):
    errors.append("duplicate chapter weights")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print(f"chapter order OK: {len(rows)} numbered chapters")
