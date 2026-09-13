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


  ---
  # breakdown:

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
```
Two lists acting as stacks. `in_stack` is where new elements land. `out_stack` is where elements get popped/peeked from. Both start empty.

```python
    def push(self, x: int) -> None:
        self.in_stack.append(x)
```
Pushing is always trivial — just drop `x` on top of `in_stack`. `.append()` is a stack's "push to top" operation. No need to touch `out_stack` at all here; the reordering work is deferred until someone actually asks to pop or peek.

```python
    def _transfer_if_needed(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```
This is the core trick, so let's slow down.

- `if not self.out_stack:` — only do work if `out_stack` is currently empty. If it already has elements, they're already in the correct front-to-back order from a previous transfer, so leave them alone.
- `while self.in_stack:` — drain `in_stack` completely.
- `self.in_stack.pop()` — removes and returns the **top** (most recently pushed) element of `in_stack`.
- `self.out_stack.append(...)` — pushes that element onto `out_stack`.

Walk through an example: say pushes happened in order 1, 2, 3, so `in_stack = [1, 2, 3]` (3 is on top). The while loop pops 3 first → `out_stack = [3]`, then pops 2 → `out_stack = [3, 2]`, then pops 1 → `out_stack = [3, 2, 1]`. Now **1 is on top of `out_stack`** — and 1 was the *first* element ever pushed. That's exactly FIFO order. The act of popping everything off one stack and pushing it onto another **reverses** the order, which is precisely what converts "last-in-first-out" into "first-in-first-out."

```python
    def pop(self) -> int:
        self._transfer_if_needed()
        return self.out_stack.pop()
```
Make sure `out_stack` is populated correctly (transfer only happens if it's empty — see above), then pop its top, which is the oldest queued element.

```python
    def peek(self) -> int:
        self._transfer_if_needed()
        return self.out_stack[-1]
```
Same idea, but just look at the top (`[-1]`) without removing it.

```python
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
```
The queue is only empty if **both** stacks are empty — an element could currently be sitting in either one depending on whether a transfer has happened recently.

**Why this is O(1) amortized, not O(1) worst-case:**

A single call to `_transfer_if_needed` can move many elements at once (O(n) in that one call). But here's the key insight: once an element is moved from `in_stack` to `out_stack`, it never moves back. Each element gets pushed to `in_stack` once, transferred once, and popped from `out_stack` once — 3 total operations across its entire lifetime, no matter how many `pop`/`peek` calls happen around it. Spread that cost over all the calls and each one averages out to O(1), even though any individual call's actual runtime varies.

**Trace through the example from the problem:**
- `push(1)` → `in_stack=[1]`, `out_stack=[]`
- `push(2)` → `in_stack=[1,2]`, `out_stack=[]`
- `peek()` → `out_stack` empty, transfer: `in_stack=[]`, `out_stack=[2,1]` → return `out_stack[-1]` = `1` ✓
- `pop()` → `out_stack` not empty, skip transfer → `out_stack.pop()` = `1`, now `out_stack=[2]` ✓
- `empty()` → `in_stack=[]` and `out_stack=[2]` → `not [] and not [2]` = `True and False` = `False` ✓
