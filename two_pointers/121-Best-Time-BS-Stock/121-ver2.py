from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxP = 0

        for i in prices:
            maxP = max(maxP, i - minPrice)
            if i < minPrice:
                minPrice = i

        return maxP
