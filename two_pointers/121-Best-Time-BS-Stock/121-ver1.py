from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxP = max(prices[right] - prices[left], maxP)
            else:
                left = right
            right += 1

        return maxP


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]

        for p in prices:
            if p < lowest:
                lowest = p

            maxP = max(p - lowest, maxP)

        return maxP
