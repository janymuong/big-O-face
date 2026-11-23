# notes — reverse linked list

**approach:**

**time complexity:**
**space complexity:**

**gotchas / follow-ups:**

Walk the list, pointing each node backwards. Save cur.next before overwriting it. When cur runs out, prev is the new head. O(n) time, O(1) space.