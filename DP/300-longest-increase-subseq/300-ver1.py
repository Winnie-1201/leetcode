from ast import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = [nums[i], count]
        dp = [1] * len(nums)
        # res = 1

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    # print(dp, i, j, nums[i], nums[j])
                    dp[i] = max(dp[i], dp[j] + 1)
                    # res = max(res, dp[i])
        # print(dp)
        return max(dp)
