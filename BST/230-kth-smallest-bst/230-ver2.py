# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = []
        result = []

        def helper(root, k, result):
            if not root:
                return

            helper(root.left, k, result)
            result.append(root.val)
            helper(root.right, k, result)

        helper(root, k, result)
        return result[k-1]

# solved!
# used the same method as the first time did it: inorder traverse
