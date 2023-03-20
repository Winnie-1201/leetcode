from ast import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return nums[0] >= goal

        # dynamic programming: time limit excceed
#         dp = [False] * len(nums)
#         dp[len(nums) - 1] = True

#         for i in range(len(nums) - 2, -1, -1):
#             # print(i)
#             for j in range(nums[i]):
#                 # print(i, j, nums[i])
#                 if i + j + 1 < len(nums) and dp[i + j + 1]:
#                     dp[i] = True
#                     break
#         # print(dp)
#         return dp[0]
