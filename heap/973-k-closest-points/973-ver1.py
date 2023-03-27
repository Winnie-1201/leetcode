from ast import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        idx = []
        for p in points:
            dis = p[0] ** 2 + p[1] ** 2
            idx.append([dis, p])

        heapq.heapify(idx)
        res = []
        for i in range(k):
            res.append(heapq.heappop(idx)[1])
        return res

        # the following does not work
        # idx did not change after heapify
        # but when calling heappop: it will return the smallest element in idx

#         idx = []
#         for p in points:
#             dis = (abs(p[0] - 0) ** 2) + (abs(p[1] - 0) ** 2)
#             heapq.heappush(idx, (dis, p))

#         res = []
#         for i in range(k):
        # change line 31 to res.append(heapq.heappop(idx)[1]) will work
#             res.append(idx[i][1])
#         return res
