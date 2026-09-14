"""
binary tree postorder traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)            # left subtree first
            dfs(node.right)           # then right subtree
            result.append(node.val)   # visit root last

        dfs(root)
        return result

    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # trick: postorder (left, right, root) is just the REVERSE of
        # "root, right, left" — which is preorder with the push order
        # of children flipped. build that modified-preorder list with a
        # stack (same shape as the iterative preorder solution), then
        # reverse it at the end.
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            # push left first so right gets popped (and visited) first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]


# --- helpers for manual testing ---
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
    print(sol.postorderTraversal(root1))            # [3, 2, 1]
    print(sol.postorderTraversalIterative(root1))   # [3, 2, 1]

    root2 = build([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print(sol.postorderTraversal(root2))            # [4, 6, 7, 5, 2, 9, 8, 3, 1]
    print(sol.postorderTraversalIterative(root2))   # [4, 6, 7, 5, 2, 9, 8, 3, 1]

    print(sol.postorderTraversal(None))             # []
    print(sol.postorderTraversal(build([1])))       # [1]