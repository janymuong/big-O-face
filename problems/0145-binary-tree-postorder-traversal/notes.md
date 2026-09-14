# notes — binary tree postorder traversal

**approach:**
postorder means "left, right, root" — visit both children completely
before the node itself.

*recursive:* mirror of preorder, just move the `result.append(node.val)`
line to the end, after both recursive calls instead of before them.

*iterative — the reverse-preorder trick:* a direct iterative postorder
(single stack, correct order first try) is genuinely awkward, because
you need to know whether you've already returned from a node's right
child before you're allowed to visit the node itself — that requires
extra state (like remembering the previously visited node) that
preorder/inorder don't need.

the clean workaround: postorder (`left, right, root`) is exactly the
**reverse** of `root, right, left`. and `root, right, left` is just
preorder with the push order flipped — push `left` before `right`
instead of `right` before `left`, so `right` pops (and gets visited)
first. build that list with the same iterative-preorder skeleton, then
reverse the whole result at the end with `result[::-1]`.

**time complexity:** O(n) for both versions — every node visited once.
**space complexity:** O(h) for the recursion stack / explicit stack list
(h = tree height), plus O(n) for the `result` list itself in the
iterative version (reversing a list is O(n) but doesn't change the
overall space complexity class).

**gotchas / follow-ups:**
- don't try to "just reverse preorder's output" — preorder's push order
  is left-then-right (so right is visited last); this trick needs the
  **opposite** push order (right-then-left) to produce root-right-left,
  which is what actually reverses cleanly into left-right-root.
- the genuinely single-pass iterative version (no reverse step) uses a
  stack plus a `last_visited` pointer to detect "have I already
  returned from this node's right subtree" — more code, same result;
  worth doing once as an exercise but the reverse trick is what most
  people reach for in practice.
- this problem's follow-up ("could you do it iteratively?") is the
  whole point of the exercise — the recursive solution is one line
  different from preorder/inorder, so make sure the iterative approach
  is the part that's actually understood, not just memorized.