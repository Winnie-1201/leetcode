# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # helper function is going to check
        # the tree started with each node
        # would be the same as the subRoot
        def helper(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2

            if node1.val != node2.val:
                return False

            return helper(node1.left, node2.left) and helper(node1.right, node2.right)

        if helper(root, subRoot):
            return True
        # for the case [1, 1], [1]
        # after comparing the root -> not qualify, then need to
        # compare the root.left with the subRoot
        # so needs to call the function itself instead of calling helper
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
