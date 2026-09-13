# notes — implement queue using stacks

**approach:**
two stacks: `in_stack` for pushes, `out_stack` for pops/peeks. pushing is
always just an append to `in_stack` — O(1), no rearranging needed.

the trick is reversing order only when necessary: a stack pops
last-in-first-out, but a queue needs first-in-first-out, so if you popped
straight off `in_stack` you'd get the newest element, not the oldest.
instead, whenever `out_stack` is empty and we need to pop/peek, dump all
of `in_stack` onto `out_stack` one at a time — this reverses the order,
so the oldest pushed element ends up on top of `out_stack`, ready to pop.
as long as `out_stack` still has elements, reuse it without touching
`in_stack` again.

**time complexity:** O(1) amortized per operation. `push` is always O(1).
`pop`/`peek` are O(1) amortized — each element gets moved from
`in_stack` to `out_stack` at most once across its whole lifetime, even
though a single call to `_transfer_if_needed` can look like O(n) in the
worst case (transferring everything at once).
**space complexity:** O(n) total across both stacks for n elements
currently in the queue.

**gotchas / follow-ups:**
- the "amortized O(1)" claim only holds because we only transfer when
  `out_stack` is empty — if you transferred on every pop/peek call
  regardless, you'd be back to O(n) per operation.
- `empty()` must check both stacks, not just one — elements could be
  sitting in either depending on transfer history.
- reverse follow-up (LeetCode 225, "Implement Stack using Queues") is
  the same idea flipped: costs more per push instead of per pop, since
  queues can't cheaply access their back.