from ast import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Time Limit Exceeded
        currGas = 0
        res = -1
        for i in range(len(gas)):
            # currGas += gas[i]

            c = i
            while c < len(gas) or c % len(gas) < i:
                newCost = cost[c % len(gas)] if c >= len(gas) else cost[c]
                newGas = gas[c % len(gas)] if c >= len(gas) else gas[c]

                currGas += newGas

                # print(currGas, newGas, newCost, c, i)
                if currGas - newCost >= 0:
                    currGas -= newCost
                    c += 1
                else:
                    currGas = 0
                    c = i
                    break
            # print(c, i)
            if c != i:
                res = i
        return res

# solution


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total, res = 0, 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
        return res
