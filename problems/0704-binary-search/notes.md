# notes — binary search

**approach:**

**time complexity:**
**space complexity:**

**gotchas / follow-ups:**


Halve the search range each time. Use lo <= hi so a single remaining element is checked, and use mid + 1 and mid - 1 so the range always shrinks. O(log n).