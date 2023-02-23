# Definition for a binary tree node.
from ast import List
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = [[root.val]]

        queue = collections.deque([root])

        while queue:

            temp = collections.deque([])
            intList = []
            while queue:
                curr = queue.popleft()
                if curr.left:
                    temp.append(curr.left)
                    intList.append(curr.left.val)
                if curr.right:
                    temp.append(curr.right)
                    intList.append(curr.right.val)
            queue = temp
            if len(intList) > 0:
                result.append(intList)

        return result
