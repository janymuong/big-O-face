"""
reverse linked list
https://leetcode.com/problems/reverse-linked-list/description/
"""

from __future__ import annotations


# definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        ''' iterative solution
        Time complexity: O(n)
        Space complexity: O(1)'''
        prev = None
        cur = head
        while cur:
            nxt = cur.next   # save the rest of the list
            cur.next = prev  # flip the pointer
            prev = cur       # advance prev
            cur = nxt        # advance cur
        return prev          # prev is the new head (None if list was empty)

    def reverseListRecursive(self, head: ListNode | None) -> ListNode | None:
        ''' recursive solution
        Time complexity: O(n)
        Space complexity: O(n) - due to the recursive call stack'''
        if not head or not head.next:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head  # the node after head now points back to head
        head.next = None       # head becomes the tail
        return new_head


# helpers for local testing
def build(vals: list[int]) -> ListNode | None:
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    cases = [[1, 2, 3, 4, 5], [2, 1], [1], []]
    for vals in cases:
        assert to_list(sol.reverseList(build(vals))) == vals[::-1]
        assert to_list(sol.reverseListRecursive(build(vals))) == vals[::-1]
        print(vals, "->", to_list(sol.reverseList(build(vals))))