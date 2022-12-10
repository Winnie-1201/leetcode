# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        res = queue[0].val

        while queue:
            temp = []

            while queue:
                curr = queue.pop(0)

                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)

            if temp:
                res = temp[0].val
            queue = temp
        return res
