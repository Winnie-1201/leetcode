class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for i in range(n - 1):
            temp = first
            first = first + second
            second = temp

        return first
#         def helper(n):
#             if n == 1:
#                 return 1
#             if n == 0:
#                 return 1

#             fn = helper(n - 1) + helper(n - 2)

#             return fn

#         return helper(n)
