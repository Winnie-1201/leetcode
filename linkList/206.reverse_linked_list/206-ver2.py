# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nxt = head.next
        curr = head
        prev = None
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        return curr

        # another way:
        # if not head or not head.next: return head
        # nxt = head
        # curr = head
        # prev = None
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
