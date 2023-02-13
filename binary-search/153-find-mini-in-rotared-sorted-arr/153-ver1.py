from ast import List

# solved it in 20 mins


class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[left] < nums[mid] and nums[mid] > nums[right]:
                small = min(nums[left], nums[right])
                mini = min(mini, small)
                left = mid
            else:
                small = min(nums[left], nums[right])
                mini = min(small, mini)
                right = mid

        return mini
