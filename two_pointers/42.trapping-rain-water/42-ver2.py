from ast import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if height[left + 1] <= leftMax and height[left + 1] <= rightMax and height[right - 1] <= leftMax and height[right - 1] <= rightMax:
                res += min(leftMax, rightMax) - height[left + 1]
                left += 1
            # if height[right - 1] < leftMax and height[right - 1] < rightMax:
                res += min(leftMax, rightMax) - height[right - 1]
                right -= 1
            else:
                left += 1
                right -= 1
                leftMax = max(leftMax, height[left])
                rightMax = max(rightMax, height[right])

        return res
        # if left == 0 and height[left] == 0: left += 1


# solved it after watching the explanation
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] < leftMax and height[left] < rightMax:
                    res += min(leftMax, rightMax) - height[left]
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                if height[right] < leftMax and height[right] < rightMax:
                    res += min(leftMax, rightMax) - height[right]
                rightMax = max(rightMax, height[right])

        return res

# cleaner solution


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
