from ast import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)  # return a hashMap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()  # [cnt, time]
        while maxHeap or queue:
            # print(queue, time, maxHeap)
            time += 1
            if maxHeap:
                h = heapq.heappop(maxHeap) + 1
                if h:
                    queue.append([h, time + n])
#             if maxHeap:
#                 h = heapq.heappop(maxHeap) + 1
#             time += 1
#             # does not work because h can be stored from the previous excution
#             if h:
#                 queue.append([h, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
