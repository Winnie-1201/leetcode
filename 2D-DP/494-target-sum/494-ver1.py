from ast import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0

            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx, total)] = helper(idx + 1, total + nums[idx]) + \
                helper(idx + 1, total - nums[idx])
            return dp[(idx, total)]

        return helper(0, 0)

        # time limit excessed
#         res = [0]

        # def helper(i, s):
        #     # print(i, s)
        #     if i == len(nums):
        #         if s == target:
        #             res[0] += 1
        #     else:
        #         helper(i + 1, s - nums[i])
        #         helper(i + 1, s + nums[i])

        # helper(0, 0)
        # return res[0]
