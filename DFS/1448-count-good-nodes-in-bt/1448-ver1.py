# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        # result = 1
        currMax = root.val

        def helper(node, currMax):
            if not node:
                return 0

            res = 1 if node.val >= currMax else 0
            if node.val >= currMax:
                currMax = node.val
            left = helper(node.left, currMax)
            right = helper(node.right, currMax)

            return res + left + right

        return helper(root, currMax)
