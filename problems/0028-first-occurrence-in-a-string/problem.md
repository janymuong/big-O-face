---
number: 28
title: "find the index of the first occurrence in a string"
difficulty: easy
tags: [string, two-pointer, string-matching]
url: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
---

## problem

given two strings `needle` and `haystack`, return the index of the first
occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

## examples
```
input: haystack = "sadbutsad", needle = "sad"
output: 0
explanation: "sad" occurs at index 0 and 6. The first occurrence is at
index 0, so we return 0.

input: haystack = "leetcode", needle = "leeto"
output: -1
explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## constraints

- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.
