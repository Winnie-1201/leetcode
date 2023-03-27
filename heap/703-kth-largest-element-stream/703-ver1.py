from ast import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # works but very slow
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# time: O(n * log(n) + m * log(k))

# heapq.heapify: O(N)
# remove element from the heap: log(N) and operate N time => N * log(N)
# run time for the constructor: O(N + N * log(N)) = O(N * log(N))


# add():
# remove and add in a heap: O(2 * log(k)) = O(log(k))
# and operate M times:
