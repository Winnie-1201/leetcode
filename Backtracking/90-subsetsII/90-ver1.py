from ast import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtract(idx):
            if idx == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            backtract(idx + 1)

            subset.pop()
            while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
                idx += 1
            backtract(idx + 1)

        backtract(0)

        return res
