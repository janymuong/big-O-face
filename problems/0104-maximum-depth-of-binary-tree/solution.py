"""
maximum depth of binary tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

# fefinition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()
    # quick manual check while iterating
    print(sol.maxDepth(None))