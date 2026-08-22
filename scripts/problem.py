#!/usr/bin/env python3
"""
scaffold a new LeetCode problem directory.

usage:
    python scripts/problem.py 42 "trapping rain water" \
        --difficulty hard \
        --tags array,two-pointer,dp \
        --url https://leetcode.com/problems/trapping-rain-water/

creates:
    problems/0042-trapping-rain-water/problem.md
    problems/0042-trapping-rain-water/solution.py
    problems/0042-trapping-rain-water/notes.md

also merges the tags into tags.json at the repo root and, unless
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
    parser = argparse.ArgumentParser(description="scaffold a new problem folder.")
    parser.add_argument("number", type=int, help="LeetCode problem number")
    parser.add_argument("title", help="relative path to the problem directory")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium")
    parser.add_argument("--tags", default="", help="comma-separated tags, e.g. array,two-pointer")
    parser.add_argument("--url", default="", help="link to the problem on LeetCode")
    parser.add_argument("--no-index", action="store_true", help="skip regenerating README.md")
    args = parser.parse_args()

    title = args.title.lower()
    difficulty = args.difficulty.lower()

    padded = f"{args.number:04d}"
    slug = slugify(title)
    folder = PROBLEMS_DIR / f"{padded}-{slug}"

    if folder.exists():
        print(f"error: {folder} already exists.", file=sys.stderr)
        sys.exit(1)

    folder.mkdir(parents=True)

    tags = [t.strip().lower() for t in args.tags.split(",") if t.strip()]

    # create the problem markdown file
    problem_md = f"""---
number: {args.number}
title: "{title}"
difficulty: {difficulty}
tags: [{", ".join(tags)}]
url: {args.url}
---

## problem

<!-- paste the problem statement / examples / constraints here -->

## examples

```
Input:
Output:
```
"""
    (folder / "problem.md").write_text(problem_md)

    if TEMPLATE.exists():
        code = TEMPLATE.read_text().format(title=title, url=args.url)
    else:
        code = f'"""\n{title}\n{args.url}\n"""\n'
    (folder / "solution.py").write_text(code)

    notes_md = f"""# notes — {title}

**approach:**

**time complexity:**
**space complexity:**

**gotchas / follow-ups:**
"""
    (folder / "notes.md").write_text(notes_md)

    if tags:
        all_tags = load_tags()
        all_tags[padded] = tags
        save_tags(all_tags)

    print(f"created {folder.relative_to(ROOT)}/")

    if not args.no_index:
        update_index = ROOT / "scripts" / "update_index.py"
        if update_index.exists():
            subprocess.run([sys.executable, str(update_index)], check=True)


if __name__ == "__main__":
    main()