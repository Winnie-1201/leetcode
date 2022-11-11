# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        count = count - n
        if count == 0:
            return head.next
        temp = head
        while temp.next:
            count -= 1
            if (count <= 0):
                temp.next = temp.next.next
                return head
            temp = temp.next

        # slow and fast pointers method:
        # slow, fast = head, head
        # for i in range(n): fast = fast.next

        # if not fast: return head.next

        # while fast.next:
        #     slow, fast = slow.next, fast.next
        # slow.next = slow.next.next

        # return head
