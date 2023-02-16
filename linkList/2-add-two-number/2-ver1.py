# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #         need: res: ListNode
        #               flag: number
        res = ListNode()
        result = res
        temp = 0
        # flag = 0
        # loop through l1 or l2
        while l1 and l2:
            flag = l1.val + l2.val + temp

            res.next = ListNode(flag % 10)
            res = res.next

            temp = flag // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            flag = l1.val + temp
            res.next = ListNode(flag % 10)
            res = res.next
            temp = flag // 10
            l1 = l1.next

        while l2:
            flag = l2.val + temp
            res.next = ListNode(flag % 10)
            res = res.next
            temp = flag // 10
            l2 = l2.next

        if temp > 0:
            res.next = ListNode(temp)
        return result.next

# [9, 9, 9]
# [9, 9]

# flag: 18 -> 19 -> 10
# temp: 1
# res: null -> 8 -> 9 -> 0 -> 1
# l1:
# l2:


# clearer:
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    result = res
    temp = 0
    # loop through l1 or l2
    while l1 or l2 or temp:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        res.next = ListNode((v1 + v2 + temp) % 10)
        res = res.next

        temp = (v1 + v2 + temp) // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next
