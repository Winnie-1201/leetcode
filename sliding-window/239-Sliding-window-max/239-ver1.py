from ast import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        res = []
        left, right, maxNum = 0, 0, nums[0]

        if len(nums) <= 1 or k <= 1:
            return nums

        while right < len(nums):
            numMap[right] = nums[right]
            maxNum = max(nums[right], maxNum)
            if right - left >= k - 1:
                del numMap[left]
                res.append(maxNum)
                left += 1

                maxNum = max(numMap.values())
                # maxNum = sorted(numMap.values(), reverse=True)[0]

                # if maxNum == nums[left]:
                #     left += 1
                #     maxNum = max(nums[left], nums[right])
                # else: left += 1
            right += 1

        return res

#  Time Limit Exceeded

# other solution


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque([])
        res = []
        left = right = 0

        while right < len(nums):
            while queue and nums[right] > queue[-1]:
                queue.pop()
            queue.append(nums[right])

            if right - left + 1 == k:
                res.append(queue[0])
                if nums[left] == queue[0]:
                    queue.popleft()
                left += 1

            right += 1

        return res
