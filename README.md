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
## workflow:
```bash
python scripts/problem.py 42 "Trapping Rain Water" \
  --difficulty Hard \
  --tags array,two-pointer,dp \
  --url https://leetcode.com/problems/trapping-rain-water/
```

---
## psets/db
<!-- INDEX:START -->
<!-- INDEX:END -->