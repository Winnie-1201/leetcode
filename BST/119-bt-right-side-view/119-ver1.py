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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = collections.deque([root])
        result = [root.val]
        while stack:
            temp = collections.deque([])

            while stack:
                curr = stack.popleft()
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
            if len(temp) > 0:
                result.append(temp[len(temp) - 1].val)
            stack = temp

        return result


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = collections.deque([root])

        while stack:
            stackLen = len(stack)
            rightNode = None

            # since stackLen is set to a value
            # in the for loop, update the stack
            # then outside of the for loop, the stackLen would be updated
            for i in range(stackLen):
                curr = stack.popleft()

                if curr:
                    rightNode = curr
                    stack.append(curr.left)
                    stack.append(curr.right)

            if rightNode:
                result.append(rightNode.val)

        return result
