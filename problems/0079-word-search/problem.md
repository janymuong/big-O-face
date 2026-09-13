---
number: 79
title: "word search"
difficulty: medium
tags: [backtracking, matrix, dfs]
url: https://leetcode.com/problems/word-search/
---

## problem

given an `m x n` grid of characters `board` and a string `word`, return
`true` if `word` exists in the grid.

the word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The
same letter cell may not be used more than once.

##  examples

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## constraints

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.