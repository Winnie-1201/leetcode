from ast import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
        return res
