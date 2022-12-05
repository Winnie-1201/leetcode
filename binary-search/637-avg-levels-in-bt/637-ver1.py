# Definition for a binary tree node.
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
        queue = [root]
        res = []

        while queue:
            temp = []
            sum, count = 0, 0
            while queue:
                curr = queue.pop(0)

                sum += curr.val
                count += 1

                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)

            queue = temp
            res.append(sum / count)
        return res

# use BFS
# next time: try DFS
