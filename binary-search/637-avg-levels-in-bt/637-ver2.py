# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        res = []
        queue = [root]

        while queue:
            sum, count = 0, 0
            temp = []

            while queue:
                curr = queue.pop(0)
                sum += curr.val
                count += 1
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
            res.append(sum/count)
            queue = temp

        return res

# solved it!
