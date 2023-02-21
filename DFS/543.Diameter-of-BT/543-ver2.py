# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            self.result = max(self.result, left + right)

            return 1 + max(left, right)

        helper(root)

        return self.result
