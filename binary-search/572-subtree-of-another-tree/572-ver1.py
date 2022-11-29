# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root, subRoot):
            if not root or not subRoot:
                return not root and not subRoot

            return root.val == subRoot.val and helper(root.left, subRoot.left) and helper(root.right, subRoot.right)

        if not root:
            return False
        # if not subRoot: return True

        if helper(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
