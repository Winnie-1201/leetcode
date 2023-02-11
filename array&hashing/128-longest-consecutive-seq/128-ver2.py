from ast import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) <= 1: return len(nums)
        numSet = set(nums)
        lgst = 0

        for i in nums:
            curr_count = 1
            if i - 1 not in numSet:
                start = i
                while start + 1 in numSet:
                    curr_count += 1
                    start += 1

            # print(newSet)
            lgst = max(lgst, curr_count)

        return lgst
