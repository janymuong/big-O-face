# notes — word search

**approach:**
dfs + backtracking from every cell that matches `word[0]`. at each step,
try to extend the match to the current cell: if it matches `word[i]`,
temporarily mark the cell as visited (overwrite with a sentinel like
`"#"` since it can't otherwise appear in the board), recurse into all 4
neighbors looking for `word[i+1]`, then restore the original character
before returning — that restoration is what makes it "backtracking"
instead of a one-shot dfs. base case: `i == len(word)` means every
character matched.

**time complexity:** O(m * n * 4^L) worst case, where L = len(word) —
for each of the m*n starting cells, the dfs can branch up to 4 ways per
character of the word. constraints keep this small (m, n <= 6, L <= 15)
so it's fine in practice even though the bound looks scary.
**space complexity:** O(L) for the recursion stack depth (bounded by
word length), ignoring input storage. no extra visited-set needed since
the in-place `"#"` marking IS the visited tracking.

**gotchas / follow-ups:**
- marking in-place and restoring afterward avoids allocating a separate
  `visited` set/grid per path — nice space win, but only works because
  we're allowed to mutate `board` and guaranteed to undo every mutation
  before returning up the call stack.
- a common early-exit optimization: before the full search, count letter
  frequencies in `board` vs `word` — if `word` needs more of some letter
  than the board has, return `false` immediately without searching.
- follow-up variant "word search II" (multiple words) needs a trie so you
  share prefixes across dfs instead of re-searching from scratch per word.