# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # first element of preorder must be the root
        root = TreeNode(preorder[0])
        # find the index of preorder[0] in inorder
        # then the left side of mid would be the left subtree
        # the right side of the mid would be the right subtree
        mid = inorder.index(preorder[0])

        # mid determines how many nodes in the left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
