from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # newSet = set(nums)
        # return len(newSet) != len(nums)
        newSet = set()
        for i in nums:
            if i in newSet:
                return True
            else:
                newSet.add(i)
        return False
