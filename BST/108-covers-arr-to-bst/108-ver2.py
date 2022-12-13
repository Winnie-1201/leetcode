# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums)//2
        left = nums[0: mid]
        right = nums[mid + 1:]

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root

# solved
