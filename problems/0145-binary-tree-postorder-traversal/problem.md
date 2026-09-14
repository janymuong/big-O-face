---
number: 145
title: "binary tree postorder traversal"
difficulty: easy
tags: [tree, dfs, stack, binary-tree]
url: https://leetcode.com/problems/binary-tree-postorder-traversal/
---

## problem

given the `root` of a binary tree, return the postorder traversal of its
nodes' values.

## examples

```
Input: root = [1,null,2,3]
Output: [3,2,1]

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

## constraints

- the number of the nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## follow up

recursive solution is trivial, could you do it iteratively?