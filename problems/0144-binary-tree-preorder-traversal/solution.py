"""
binary tree preorder traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            result.append(node.val)  # visit root first
            dfs(node.left)           # then left subtree
            dfs(node.right)          # then right subtree

        dfs(root)
        return result

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            # push right first so left gets popped (and processed) first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


# --- helpers for manual testing (build tree from a
# level-order list with "null" gaps, using index-based children) ---
def build(values):
    if not values or values[0] is None:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(kids, None)
            node.right = next(kids, None)
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()

    root1 = build([1, None, 2, 3])
    print(sol.preorderTraversal(root1))            # [1, 2, 3]
    print(sol.preorderTraversalIterative(root1))    # [1, 2, 3]

    root2 = build([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print(sol.preorderTraversal(root2))             # [1, 2, 4, 5, 6, 7, 3, 8, 9]
    print(sol.preorderTraversalIterative(root2))    # [1, 2, 4, 5, 6, 7, 3, 8, 9]

    print(sol.preorderTraversal(None))              # []
    print(sol.preorderTraversal(build([1])))        # [1]