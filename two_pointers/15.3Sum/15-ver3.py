from ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                elif nums[start] + nums[end] == 0 - nums[i]:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > 0 - nums[i]:
                    end -= 1
                else:
                    start += 1

        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:
                threeSum = nums[i] + nums[start] + nums[end]

                if threeSum > 0:
                    end -= 1
                elif threeSum < 0:
                    start += 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

        return res
