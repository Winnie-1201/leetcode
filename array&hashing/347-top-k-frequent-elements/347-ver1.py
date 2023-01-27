# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.

from ast import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
#       res.get: to get the value
#       sorted based on the value
        return sorted(res, key=res.get, reverse=True)[:k]
        # print(sorted(res, key=res.get, reverse=True))
#

        # if len(nums) <= 1: return nums
        # res = []
        # count = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]: count += 1
        #     else:
        #         if count >= k:
        #             res.append(nums[i-1])
        #         count = 1
        # return res
