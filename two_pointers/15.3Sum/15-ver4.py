from ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                # print(nums[i], nums[i - 1], i)
                continue
            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                elif right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # print(left, right)
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res
