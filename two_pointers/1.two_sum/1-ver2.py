from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        start = 0
        while start < len(nums):
            rm = target - nums[start]
            rest = nums[start+1:]
            # print(rest, rm)

            if rm in rest:
                return [start, rest.index(rm)+start+1]

            start += 1
