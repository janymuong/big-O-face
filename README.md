# big-O-face
> algo-rhythms

```sh
# algorhythms
 
├── README.md              # auto-generated index (script updates this)
├── template.py            # boilerplate for new problems
├── problems/
│   ├── 0001-two-sum/
│   │   ├── problem.md     # question, link, constraints, examples
│   │   ├── solution.py    # code
│   │   └── notes.md       # approach, complexity, gotchas, follow-ups
│   ├── 0002-add-two-numbers/
│   │   └── ...
├── scripts/
│   ├── problem.py         # gets me a new problem folder from template
│   └── update_index.py    # regenerates README.md table from problem.md files
└── tags.json              # optional: problem# -> [tags] for filtering by topic
```

---
## script:
> and you have to follow the script, always :)

```bash
python scripts/problem.py 42 "trapping rain water" \
  --difficulty hard \
  --tags array,two-pointer,dp \
  --url https://leetcode.com/problems/trapping-rain-water/
```

---
## psets/db
<!-- INDEX:START -->
| # | title | difficulty | tags | solution |
|---|-------|------------|------|----------|
| 21 | [merge two sorted lists](https://leetcode.com/problems/merge-two-sorted-lists/) | easy | linked-list, recursion | [solution](problems/0021-merge-two-sorted-lists/solution.py) |
| 73 | [certain problem](https://leetcode.com/problems/) | hard | array, two-pointer, dp | [solution](problems/0073-certain-problem/solution.py) |
<!-- INDEX:END -->