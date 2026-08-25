# notes — find the index of the first occurrence in a string

**approach:**
slide a window of length `len(needle)` across `haystack`, comparing the
slice at each start index. python's string equality check under the hood
is c-optimized, so this is fast in practice even though it's not the
asymptotically optimal algorithm.

**time complexity:** O(n * m) worst case (n = len(haystack), m =
len(needle)) — e.g. haystack = "aaaa...a", needle = "aaa...ab". fine here
since constraints cap both at 10^4.
**space complexity:** O(1) extra (slicing creates a temp string of size m
per comparison, not counted as persistent extra space)

**gotchas / follow-ups:**
- `str.find()` would solve this in one line — but the point is practicing the algorithm.
- true O(n + m) solution is KMP (Knuth-Morris-Pratt): build a "failure
  function" / prefix table for `needle` so that on a mismatch you never re-scan characters of `haystack` you've already matched. worth
  implementing separately as a follow-up since it's a classic pattern
  that resurfaces (e.g. repeated substring pattern, shortest palindrome).
- rabin-karp (rolling hash) is another O(n + m) average-case approach, good to know for string-matching problems with multiple needles.