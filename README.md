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
  --url https://leetcode.com/problems/trapping-rain-water/ \
  # --no-index stops table updates to stop growth of it
```

---
## psets/db
<!-- INDEX:START -->
| # | title | difficulty | tags | solution |
|---|-------|------------|------|----------|
| 20 | [valid parentheses](https://leetcode.com/problems/valid-parentheses/description/) | easy | string, stack, bracket sequences | [solution](problems/0020-valid-parentheses/solution.py) |
| 21 | [merge two sorted lists](https://leetcode.com/problems/merge-two-sorted-lists/) | easy | linked-list, recursion | [solution](problems/0021-merge-two-sorted-lists/solution.py) |
| 28 | [find the index of the first occurrence in a string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | easy | string, two-pointer, string-matching | [solution](problems/0028-first-occurrence-in-a-string/solution.py) |
| 79 | [word search](https://leetcode.com/problems/word-search/) | medium | backtracking, matrix, dfs | [solution](problems/0079-word-search/solution.py) |
| 125 | [valid palindrome](https://leetcode.com/problems/valid-palindrome/description/) | easy | two-pointer, string | [solution](problems/0125-valid-palindrome/solution.py) |
| 144 | [binary tree preorder traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | easy | tree, dfs, stack, binary-tree | [solution](problems/0144-binary-tree-preorder-traversal/solution.py) |
| 145 | [binary tree postorder traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | easy | tree, dfs, stack, binary-tree | [solution](problems/0145-binary-tree-postorder-traversal/solution.py) |
| 146 | [lru cache](https://leetcode.com/problems/lru-cache/) | medium | hash-map, linked-list, doubly-linked-list, design | [solution](problems/0146-lru-cache/solution.py) |
| 217 | [contains duplicate](https://leetcode.com/problems/contains-duplicate) | easy | array, hash table, sorting | [solution](problems/0217-contains-duplicate/solution.py) |
| 232 | [implement queue using stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | easy | stack, queue, design | [solution](problems/0232-implement-queue-using-stacks/solution.py) |
| 242 | [valid anagram](https://leetcode.com/problems/valid-anagram/description/) | easy | string, hash table, sorting | [solution](problems/0242-valid-anagram/solution.py) |
| 283 | [move zeroes](https://leetcode.com/problems/move-zeroes/description/) | easy | array, two pointers | [solution](problems/0283-move-zeroes/solution.py) |
| 387 | [first unique character in a string](https://leetcode.com/problems/first-unique-character-in-a-string/description/) | easy | hash table, string, queue, counting | [solution](problems/0387-first-unique-character-in-a-string/solution.py) |
| 393 | [utf-8 validation](https://leetcode.com/problems/utf-8-validation/) | medium | character arrays | [solution](problems/0393-utf-8-validation/solution.py) |
| 704 | [binary search](https://leetcode.com/problems/binary-search/description/) | easy | array, binary search | [solution](problems/0704-binary-search/solution.py) |
<!-- INDEX:END -->