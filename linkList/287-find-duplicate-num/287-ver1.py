from ast import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time Limit Exceeded
        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]: return nums[i]

        numsSet = set()

        for i in nums:
            if i in numsSet:
                return i
            numsSet.add(i)

# Passed but with space O(n) instead of constant

# Using Floyd's cycle detection
# think it as a linked list problem


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow1 = 0
        while True:
            slow1 = nums[slow1]
            slow = nums[slow]

            if slow1 == slow:
                return slow
