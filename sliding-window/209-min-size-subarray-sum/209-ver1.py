from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = currSum = 0
        minLen = len(nums) + 1

        while right < len(nums):
            currSum += nums[right]

            while currSum >= target:
                minLen = min(minLen, right - left + 1)
                currSum -= nums[left]
                left += 1

            right += 1

        return minLen if minLen != len(nums) + 1 else 0
