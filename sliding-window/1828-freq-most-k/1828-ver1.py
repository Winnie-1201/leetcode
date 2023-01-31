from ast import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        # print(nums)

        left, right, mostFreq, total = 0, 0, 0, 0

        while right < len(nums):
            total += nums[right]
            if nums[right] * (right - left + 1) <= total + k:
                right += 1
                mostFreq = max(mostFreq, right - left)
            else:
                total -= nums[left]
                left += 1
                right += 1

        return mostFreq

# using sliding window and sorting


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        # nums = sorted(nums)
        # print(nums)
        nums.sort()

        left, right, mostFreq, total = 0, 0, 0, 0

        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            mostFreq = max(mostFreq, right - left + 1)
            right += 1

        return mostFreq
