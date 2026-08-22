<!-- # notes — merge two sorted lists

**approach:**

**time complexity:**
**space complexity:**

**gotchas / follow-ups:** -->

# notes — merge two sorted lists

**approach:**
dummy-head + tail pointer. walk both lists at once, always attach the
smaller current node to `tail`, then advance that list's pointer and
`tail`. when one list runs out, splice the remainder of the other list
directly onto `tail.next` (no need to keep looping node by node since
it's already sorted). return `dummy.next`.

**time complexity:** O(n + m) — each node visited once
**space complexity:** O(1) extra — reusing existing nodes, only the dummy
node is new

**gotchas / follow-ups:**
- the dummy node avoids special-casing "what if the merged list is empty"
  or "what's the head" — always return `dummy.next`.
- recursive version is also O(n+m) time but O(n+m) space from the call
  stack; iterative avoids that.
- careful with `<=` vs `<` on the comparison — doesn't affect correctness
  for stability here since nodes are equal-value interchangeable, but
  worth knowing which one you chose and why.