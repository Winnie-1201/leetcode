# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        def helper(root, arr):
            if not root:
                return

            helper(root.left, arr)
            arr.append(root.val)
            helper(root.right, arr)

        helper(root, arr)
        res = math.inf

        for i in range(len(arr)-1):
            res = min(abs(arr[i+1]-arr[i]), res)

        return res
