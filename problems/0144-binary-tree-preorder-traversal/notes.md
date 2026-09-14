# notes — binary tree preorder traversal

**approach:**
preorder means: visit the node itself, then its left subtree, then its
right subtree ("root, left, right").

*recursive:* a tiny dfs helper appends `node.val` before recursing into
`node.left` then `node.right`. base case is `node is None` → do nothing.
this mirrors the definition almost word for word.

*iterative:* simulate the call stack manually with an explicit `stack`
list. pop a node, visit it (append to result), then push its children —
**right before left**. this ordering matters: since a stack pops the
most-recently-pushed item first, pushing right first means left comes
back out on top next, preserving the "left before right" requirement
of preorder.

**time complexity:** O(n) — every node visited exactly once, both
versions.
**space complexity:** O(h) where h = tree height, for the recursion
stack (recursive) or the explicit `stack` list (iterative). worst case
O(n) for a completely skewed tree (basically a linked list), best case
O(log n) for a balanced tree.

**gotchas / follow-ups:**
- the "push right before left" trick is the classic gotcha for the
  iterative version — get it backwards and you silently produce a
  right-to-left preorder instead.
- inorder (left, root, right) and postorder (left, right, root) are the
  same dfs skeleton with the `result.append(node.val)` line moved to a
  different position — worth doing all three back-to-back to see how
  little actually changes.
- iterative postorder is the annoying one of the three (order of
  visiting doesn't match a simple single-stack pop order as cleanly),
  worth revisiting separately when that problem comes up.
- morris traversal is an O(1)-extra-space follow-up that avoids both
  recursion and an explicit stack by temporarily rewiring `right`
  pointers — overkill for this problem's constraints but a nice trick
  to know exists.