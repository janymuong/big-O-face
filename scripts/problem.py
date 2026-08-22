#!/usr/bin/env python3
"""
Scaffold a new LeetCode problem folder.

Usage:
    python scripts/new_problem.py 42 "Trapping Rain Water" \
        --difficulty Hard \
        --tags array,two-pointer,dp \
        --url https://leetcode.com/problems/trapping-rain-water/

Creates:
    problems/0042-trapping-rain-water/problem.md
    problems/0042-trapping-rain-water/solution.py
    problems/0042-trapping-rain-water/notes.md

Also merges the tags into tags.json at the repo root and, unless
--no-index is passed, regenerates README.md via update_index.py.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
TEMPLATE = ROOT / "template.py"
TAGS_FILE = ROOT / "tags.json"


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def load_tags() -> dict:
    if TAGS_FILE.exists():
        return json.loads(TAGS_FILE.read_text())
    return {}


def save_tags(data: dict) -> None:
    TAGS_FILE.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new problem folder.")
    parser.add_argument("number", type=int, help="LeetCode problem number")
    parser.add_argument("title", help="Problem title, e.g. 'Trapping Rain Water'")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"], default="Medium")
    parser.add_argument("--tags", default="", help="Comma-separated tags, e.g. array,two-pointer")
    parser.add_argument("--url", default="", help="Link to the problem on LeetCode")
    parser.add_argument("--no-index", action="store_true", help="Skip regenerating README.md")
    args = parser.parse_args()

    padded = f"{args.number:04d}"
    slug = slugify(args.title)
    folder = PROBLEMS_DIR / f"{padded}-{slug}"

    if folder.exists():
        print(f"Error: {folder} already exists.", file=sys.stderr)
        sys.exit(1)

    folder.mkdir(parents=True)

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    problem_md = f"""---
number: {args.number}
title: "{args.title}"
difficulty: {args.difficulty}
tags: [{", ".join(tags)}]
url: {args.url}
---

## Problem

<!-- paste the problem statement / examples / constraints here -->

## Examples

```
Input:
Output:
```
"""
    (folder / "problem.md").write_text(problem_md)

    if TEMPLATE.exists():
        code = TEMPLATE.read_text().format(title=args.title, url=args.url)
    else:
        code = f'"""\n{args.title}\n{args.url}\n"""\n'
    (folder / "solution.py").write_text(code)

    notes_md = f"""# Notes — {args.title}

**Approach:**

**Time complexity:**
**Space complexity:**

**Gotchas / follow-ups:**
"""
    (folder / "notes.md").write_text(notes_md)

    if tags:
        all_tags = load_tags()
        all_tags[padded] = tags
        save_tags(all_tags)

    print(f"Created {folder.relative_to(ROOT)}/")

    if not args.no_index:
        update_index = ROOT / "scripts" / "update_index.py"
        if update_index.exists():
            subprocess.run([sys.executable, str(update_index)], check=True)


if __name__ == "__main__":
    main()
