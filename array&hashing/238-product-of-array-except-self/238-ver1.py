from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        nxt = 1
        res = [1] * len(nums)
#       get the product of the previous nums
        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i]
#       get the product of the after nums
#       starts from len(nums)-1, step=-1, end at idx 0
        for i in range(len(nums)-1, -1, -1):
            res[i] *= nxt
            nxt *= nums[i]

        return res
