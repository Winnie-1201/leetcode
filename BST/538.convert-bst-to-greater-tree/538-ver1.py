# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = [root]

        while queue:
            curr = queue.pop(0)

            if curr.right:
                temp = [curr.right]

            while temp:
                right = temp.pop(0)
                right_sum += right.val

                if right.left:
                    temp.append(right.left)
                if right.right:
                    temp.append(right.right)

            curr.val = right_sum
            right_total = right_sum

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return root

        # Solution
        # if root:
        #     self.convertBST(root.right)
        #     print(root.val)
        #     self.total += root.val
        #     print('total', self.total)
        #     root.val = self.total
        #     print('-----')
        #     self.convertBST(root.left)

        # return root


# Does not have a clear idea yet
# What I think: curr_node.val = curr_node.val + all values on its right side
# But I am not sure how to keep track of the values on its right side;

#
