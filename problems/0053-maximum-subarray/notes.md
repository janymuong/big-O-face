# notes — maximum subarray

**approach:**

**time complexity:**
**space complexity:**
O(n) time, O(1) space.

**gotchas / follow-ups:**
This is Kadane's algorithm. At each element, either extend the current run (cur + x) or start fresh at x if the run so far is dragging you down. Start best at nums[0], not 0, or an all-negative list returns the wrong answer. 