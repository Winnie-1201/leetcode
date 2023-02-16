# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # get the middle
        # curr = mid = head
        # while slo and curr.next:
        #     curr = curr.next.next
        #     mid = mid.next
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow stops one node before the mid
        curr = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge the first half and the second half
        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next

            first.next = second
            second.next = nxt1

            first, second = nxt1, nxt2
