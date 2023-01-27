from ast import List
import collections


# Time limit exceeded
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res = set(nums)

        hashset = collections.defaultdict(list)
        start = 0
        while start < len(nums):
            if nums[start] - 1 not in res:
                hashset[nums[start]] = 1

                seq = nums[start] + 1
                while seq in res:
                    hashset[nums[start]] += 1
                    seq += 1

                start += 1
            else:
                hashset[nums[start]] = 1
                start += 1

        return max(hashset.values())


# other solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if n is the starting num in a sequence
            if n - 1 not in nums:
                # count the length of the seq started with n
                length = 0
                # check if n + 1 in nums
                while n + length in numSet:
                    length += 1

                # get the max of each seq
                longest = max(length, longest)
        return longest
