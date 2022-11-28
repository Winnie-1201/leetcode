# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.num = 0

        def helper(root, sum=0):
            if not root:
                return 0

            sum += root.val
            if sum == targetSum:
                self.num += 1

            left = helper(root.left, sum)
            right = helper(root.right, sum)

        stack = [root]
        while stack:
            curr = stack.pop()

            helper(curr)

            if curr:
                stack.append(curr.left)
                stack.append(curr.right)

        return self.num
