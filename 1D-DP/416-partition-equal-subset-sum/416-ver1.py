from ast import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # does not work!!!
        nums.sort()
        left, mid, right = 0, 0, len(nums) - 1
        temp = 0
        temp1 = nums[right]
        while mid < right:
            temp += nums[mid]

            if temp == temp1 and mid == right - 1:
                return True
            elif temp > temp1 and mid == right - 1:
                return False
            elif temp > temp1:
                temp -= nums[left]
                temp1 += nums[left]
                left += 1
                right -= 1
            mid += 1
        return False


# correct solution:
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            new = nums[i]
            nextDP = set()

            for s in dp:
                nextDP.add(s + new)
                nextDP.add(s)
            dp = nextDP

        return True if target in dp else False
