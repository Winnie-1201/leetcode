# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
#         result = root1

#         def helper(root1, root2):

#             root1.val = root1.val + root2.val

#             if not root1.left:
#                 root1.left = root2.left
#                 return
#             if not root1.right:
#                 root1.right = root2.right
#                 return
#             if not root2.left or not root2.right: return root1


#             result.left = helper(root1.left, root2.left)
#             result.right = helper(root1.right, root2.right)

#         helper(root1, root2)
        return result
