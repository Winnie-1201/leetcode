# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def helper(root, arr):
            if not root:
                return

            helper(root.left, arr)
            arr.append(root.val)
            helper(root.right, arr)

        helper(root, arr)

        i, j = 0, len(arr)-1

        while i < j:
            if arr[i] + arr[j] == k:
                return True

            if arr[i] + arr[j] < k:
                i += 1
            else:
                j -= 1

        return False
