# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> ListNode[Optional[ListNode]]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        result = [[] for _ in range(k)]

        curr = head
        prev = head

        size, extra = count // k, count % k

        for i in range(k):
            result[i] = curr

            for j in range(size + (1 if extra > 0 else 0)):
                prev, curr = curr, curr.next
            if prev:
                prev.next = None
            extra -= 1

        return result

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
#         size = 0
#         temp = head
        # while temp:
        #     size += 1
        #     temp = temp.next

        # res = [[] for _ in range(k)]

        # count, extra = size // k, size % k

        # curr, prev = head, head

        # for i in range(k):
        #     res[i] = curr

        #     j = count + 1 if extra > 0 else count

        #     while j > 0:
        #         prev = curr
        #         curr = curr.next
        #         j -= 1

        #     if prev:
        #         prev.next = None
        #     extra -= 1

        # return res
