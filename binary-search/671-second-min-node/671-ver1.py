# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.set = set()
        if not root or not root.left or not root.right:
            return -1

        def helper(root):
            if not root:
                return

            self.set.add(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)

        if len(self.set) == 1:
            return -1
        else:
            return sorted(list(self.set))[1]

#         if not root or not root.left or not root.right: return -1

#         elif root.right.val > root.val: return root.right.val

#         elif root.left.val > root.val : return root.left.val

#         else: return -1
