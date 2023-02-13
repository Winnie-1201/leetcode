from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # print(mid, left, right)
            if nums[mid] == target:
                return mid

            # when mid is the left sorted part
            elif nums[left] <= nums[mid]:
                # if target is greater than the smallest in the left
                # then search the right part
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            # mid is the right sorted part
            else:
                # when target is greater than the largest in the right part
                # then search the left part
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

# solved it after watching the solution
