# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            return 1 + max(left, right)

        return helper(root)
