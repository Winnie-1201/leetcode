from ast import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            far = 0
            for i in range(left, right + 1):
                far = max(far, i + nums[i])
            left = right + 1
            right = far
            res += 1

        return res

        # dp is much slower
        dp = [1] * len(nums)
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            temp = dp[i] + dp[i + 1]
            for j in range(nums[i]):
                if i + j + 1 < len(nums):
                    temp = min(dp[i + j + 1] + 1, temp)

            dp[i] = temp

        return dp[0]
