from ast import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        left = 0

        for i in range(len(nums)):
            while q and nums[i] > q[len(q) - 1]:
                q.pop()
            q.append(nums[i])
            if i - left > k - 1:
                if nums[left] == q[0]:
                    q.popleft()
                left += 1
            if i >= k - 1:
                res.append(q[0])
        return res
