from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            total += n
            res = max(res, total)
            if total <= 0:
                total = 0

        return res
        # res = nums[len(nums) - 1]
        dp = [float('-inf')] * (len(nums))
        dp[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(dp[i + 1] + nums[i], nums[i])
            # res = max(res, dp[i])
        # print(dp)
        return max(dp)
