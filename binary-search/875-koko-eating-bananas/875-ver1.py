from ast import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")
        piles.sort()
        start, end = 1, piles[-1]

        while start <= end:
            mid = start + ((end - start) // 2)
            total = 0

            for i in piles:
                if mid >= i:
                    total += 1
                else:
                    total += i // mid + 1 if i % mid != 0 else i // mid
            # print(total)
            if total <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1

        return res


# clear
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        start, end = 1, max(piles)

        while start <= end:
            mid = (start + end) // 2
            total = 0

            for i in piles:
                # round up
                total += math.ceil(i / mid)
                # if mid >= i:
                #     total += 1
                # else:
                #     total += i // mid + 1 if i % mid != 0 else i // mid
            # print(total)
            if total <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1

        return res
