# notes — lru cache

**approach:**
the requirement "get and put must each run in O(1)" is the whole design
constraint. that rules out a plain list (finding/removing the LRU entry
would be O(n)) and rules out a plain hash map alone (no way to track
recency order in O(1)). the fix is combining both structures:

- a **hash map** gives O(1) key lookup.
- a **doubly linked list** gives O(1) removal/insertion at both ends,
  *given a direct reference to the node* — which the hash map provides.

keep the list ordered oldest → newest (LRU on the left near a dummy
head, MRU on the right near a dummy tail). every `get` or successful
`put` on an existing key moves that node to the tail (most recent).
every `put` that grows past capacity removes whatever's sitting right
after the dummy head (the actual LRU).

two versions here:
1. `LRUCache` — `OrderedDict`, which already implements this exact
   hash-map-plus-linked-list combo internally. `move_to_end` and
   `popitem(last=False)` do exactly what's needed in one call each.
2. `LRUCacheDLL` — the manual version, spelling out the doubly linked
   list explicitly with dummy head/tail sentinel nodes. this is closer
   to what an interviewer usually wants, since it proves you understand
   *why* it's O(1) rather than delegating to a builtin.

**time complexity:** O(1) average for both `get` and `put`, both
versions — dict lookup is O(1) average, and linked-list splice
operations are O(1) given a node reference.
**space complexity:** O(capacity) — the map and list never hold more
than `capacity` entries by construction.

**gotchas / follow-ups:**
- dummy head/tail sentinels remove every "is this the first/last real
  node" edge case — every real node always has a genuine `prev` and
  `next` to work with, never `None`. worth remembering as a pattern for
  any doubly-linked-list problem.
- classic bug: forgetting to move a node to the tail on a `get` that hits
  (not just on `put`) — a `get` is a "use" and must count toward
  recency, or the cache silently degrades into pure insertion order.
- classic bug #2: checking capacity *before* inserting the new node
  instead of after — off-by-one on eviction timing.
- follow-up variant: LFU (Least Frequently Used) cache is the natural
  next problem — same O(1) constraint, but ordering by frequency count
  instead of recency, which needs an extra layer of buckets-by-frequency.