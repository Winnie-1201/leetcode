from ast import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        temp = nums[:]
        max1, max2 = nums[len(nums) - 1], nums[len(nums) - 2]
        idx = len(nums) - 3

        while idx >= 1:
            nums[idx] = nums[idx] + max1
            max1 = max(max1, max2)
            max2 = nums[idx]
            idx -= 1

        max1 = max(max1, max2)

        max3, max4 = temp[len(temp) - 2], temp[len(temp) - 3]
        idx = len(temp) - 4

        while idx >= 0:
            temp[idx] = temp[idx] + max3
            max3 = max(max3, max4)
            max4 = temp[idx]
            idx -= 1

        max2 = max(max3, max4)

        return max(max1, max2)

        # if len(nums) <= 1: return nums[0]
        # rob1, rob2, rob3, rob4 = 0, 0, 0, 0
        # temp = nums[:]
        # for i in range(len(temp) - 1):
        #     temp[i] = max(temp[i] + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp[i]

        # for i in range(1, len(nums)):
        #     nums[i] = max(nums[i] + rob3, rob4)
        #     rob3 = rob4
        #     rob4 = nums[i]
        # # print(nums, rob4)
        # return max(rob2, rob4)


def rob(self, nums: List[int]) -> int:
    # def rob(self, nums: List[int]) -> int:
    return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


def helper(self, nums):
    rob1, rob2 = 0, 0

    for n in nums:
        newRob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2
