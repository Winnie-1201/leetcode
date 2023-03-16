from ast import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            temp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            # print(currMax, currMin)
            res = max(currMax, res)

        return res
#         if len(nums) == 1: return nums[0]
#         dp = [[1, 1] * 1 for i in range(len(nums) - 1)]
#         dp[0][0] = max(nums[0] * nums[1], nums[1])
#         dp[0][1] = min(nums[0], nums[1])
#         res = max(max(nums), dp[0][0])
#         # print(dp)
#         for i in range(2, len(nums)):
#             if nums[i] == 0:
#                 dp[i - 1] = [1, 1]
#             elif nums[i] > 0:
#                 dp[i - 1][0] = nums[i] * dp[i - 2][1]
#                 dp[i - 1][1] = nums[i] * dp[i - 2][0]
#             else:
#                 dp[i - 1][0] = nums[i] * dp[i - 2][0]
#                 dp[i - 1][1] = nums[i] * dp[i - 2][1]

#             res = max(res, dp[i - 1][0])
#         return res
