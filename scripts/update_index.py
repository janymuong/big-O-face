#!/usr/bin/env python3
"""
regenerate the problem table in README.md by scanning problems/*/problem.md.

looks for two markers in README.md:
    <!-- INDEX:START -->
    <!-- INDEX:END -->
and replaces everything between them with a fresh table. if the markers
aren't present, they (and the table) are appended to the end of the file.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
README = ROOT / "README.md"

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
FIELD_RE = re.compile(r'^(\w+):\s*(.*)$', re.MULTILINE)


def parse_problem_md(path: Path) -> dict:
    text = path.read_text()
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "tags":
            val = [t.strip() for t in val.strip("[]").split(",") if t.strip()]
        fields[key] = val.strip('"') if isinstance(val, str) else val
    return fields


def build_table() -> str:
    rows = []
    for folder in sorted(PROBLEMS_DIR.iterdir()):
        problem_md = folder / "problem.md"
        if not problem_md.exists():
            continue
        fields = parse_problem_md(problem_md)
        if not fields:
            continue
        number = fields.get("number", "?")
        title = fields.get("title", folder.name)
        difficulty = fields.get("difficulty", "")
        tags = ", ".join(fields.get("tags", []))
        url = fields.get("url", "")
        sol_link = f"{folder.name}/solution.py"
        title_cell = f"[{title}]({url})" if url else title
        rows.append((int(number) if str(number).isdigit() else 0,
                      f"| {number} | {title_cell} | {difficulty} | {tags} | [solution]({sol_link}) |"))

    rows.sort(key=lambda r: r[0])
    header = "| # | title | difficulty | tags | solution |\n|---|-------|------------|------|----------|"
    body = "\n".join(r[1] for r in rows) if rows else "| _no problems yet_ | | | | |"
    return f"{header}\n{body}"


def main():
    table = build_table()
    block = f"{START}\n{table}\n{END}"

    if README.exists():
        text = README.read_text()
    else:
        text = "# algorhythms\n\n"

    if START in text and END in text:
        text = re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            block,
            text,
            flags=re.DOTALL,
        )
    else:
        text = text.rstrip() + "\n\n" + block + "\n"

    README.write_text(text)
    print(f"modified: {README.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
