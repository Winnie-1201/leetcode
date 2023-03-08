from ast import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[len(cost) - 2], cost[len(cost) - 1]

        idx = len(cost) - 3
        while idx >= 0:
            temp = first
            first = cost[idx] + min(first, second)
            second = temp
            idx -= 1

        return min(first, second)
        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] += min(cost[i + 1], cost[i + 2])

        # return min(cost[0], cost[1])
