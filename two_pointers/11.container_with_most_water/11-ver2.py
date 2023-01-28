from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        mArea = 0

        start, end = 0, len(height) - 1

        while start < end:
            temp = (end - start) * min(height[start], height[end])

            mArea = max(temp, mArea)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return mArea
