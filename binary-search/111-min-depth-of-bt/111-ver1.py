# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):

            if root and not root.left and not root.right:
                return 1

            if not root:
                return float('inf')

            left = helper(root.left)
            right = helper(root.right)

            # print(left, right)
            return 1 + min(left, right)

        if not root:
            return 0
        return helper(root)
