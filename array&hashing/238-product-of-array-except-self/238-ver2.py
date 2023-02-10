class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        res = [1] * len(nums)
        nxt = 1

        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i]

        for i in range(len(nums) - 1, -1, -1):

            res[i] *= nxt
            nxt *= nums[i]

        return res
