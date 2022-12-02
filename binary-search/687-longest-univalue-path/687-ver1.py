# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def helper(root):
            if not root:
                return 0

            # traverse down to the left
            left = helper(root.left)
            # traverse down to the right
            right = helper(root.right)

            # declare the count of left node and right node
            left_count = right_count = 0

            # count the nodes with the same value
            if root.left and root.left.val == root.val:
                left_count = left + 1
            if root.right and root.right.val == root.val:
                right_count = right + 1

            # reassign the return count to the larger one
            self.count = max(self.count, left_count + right_count)

            # in case there is another longest path that passed through another 'head node'
            # we need to return the max of left and right
            return max(left_count, right_count)

        # call the helper function to update the count
        helper(root)
        return self.count
#         count = 0
#         def helper(root, count):
#             if root and root.left and root.val == root.left.val: count += 1
#             elif root and root.right and root.val == root.right.val: count += 1
#             if not root: return count

#             left = helper(root.left, count)
#             right = helper(root.right, count)

#             return max(left, right)

#         return helper(root, count)
