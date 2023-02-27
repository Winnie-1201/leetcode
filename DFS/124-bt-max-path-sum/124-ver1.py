# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            leftMax = max(0, left)
            rightMax = max(0, right)

            # get the result with split
            res[0] = max(res[0], leftMax + rightMax + node.val)

            # return the result without split
            return node.val + max(leftMax, rightMax)

        helper(root)

        return res[0]
