from ast import List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len%size != 0: return false
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                # print(count, i)
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
