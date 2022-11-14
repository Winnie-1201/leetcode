# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while head and head.next:
            curr = head
            nxt = head.next

            # swap two nodes by pair
            prev.next = nxt
            curr.next = nxt.next
            nxt.next = curr

            # then change the head to the next pair
            head = curr.next
            prev = curr
        return dummy.next
