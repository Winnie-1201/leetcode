from ast import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = nums[len(nums) - 1], nums[len(nums) - 2]
        idx = len(nums) - 3

        while idx >= 0:
            nums[idx] = nums[idx] + max1
            max1 = max(max1, max2)
            max2 = nums[idx]
            idx -= 1

        return max(max1, max2)
        # rob1, rob2 = 0, 0

        # for n in nums:
        #     temp = max(n + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2
