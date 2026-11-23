# notes — reverse linked list

# 206. Reverse Linked List

## Approach
Iterative, three pointers (prev, cur, nxt). Walk the list once, flipping each
node's `next` to point at the previous node.

## Complexity
- Time: O(n)
- Space: O(1) iterative, O(n) recursive (call stack)

## Gotchas
- Save `cur.next` *before* overwriting it, or you lose the rest of the list.
- Return `prev`, not `cur` (`cur` is None when the loop ends).
- Empty list and single node are handled naturally.

## Recursive idea
Reverse everything after head, then make `head.next.next = head` and
`head.next = None`.

TLDR: walk the list, pointing each node backwards. Save cur.next before overwriting it. When cur runs out, prev is the new head. O(n) time, O(1) space.