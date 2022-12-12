# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def helper(root):
            if not root:
                return 0

            if root.left and not root.left.left and not root.left.right:
                self.sum += root.left.val

            left = helper(root.left)
            right = helper(root.right)

        helper(root)
        return self.sum

# solved!
