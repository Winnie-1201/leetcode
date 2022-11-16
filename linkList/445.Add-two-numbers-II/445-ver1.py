# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        result = []
        k = 0
        # print(stack1)
        while len(stack1) > 0 and len(stack2) > 0:
            s = stack1.pop() + stack2.pop() + k
            k = 0
            if s >= 10:
                s = s % 10
                k += 1
            result.append(s)
        if k >= 1 and stack1:
            result.append(stack1.pop()+k)
        elif k >= 1 and stack2:
            result.append(stack2.pop()+k)
        elif (k >= 1):
            result.append(k)

        result.extend(stack1 if stack1 else stack2)

        dummy = ListNode()
        res = dummy
        while len(result) > 0:
            dummy.next = ListNode(result.pop())
            dummy = dummy.next
        return res.next

# 1425 / 1563 test cases passed.
# [1]
# [9,9] -- did not pass
