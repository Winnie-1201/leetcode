# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        curr = head

        # get the total len of the linked list
        while curr:
            total += 1
            curr = curr.next

        curr = ListNode()
        curr.next = head
        dummy = curr
        count = 0

        # locate the node that needs to be changed
        while curr and count < total - n:
            curr = curr.next
            count += 1

        curr.next = curr.next.next

        # # use n to locate the node at n - 2
        # dummy = ListNode(0, head)
        # left, right = dummy, head

        # while n > 0:
        #     right = right.next
        #     n -= 1

        # # use right to locate the node that needs to be change
        # while right:
        #     left = left.next
        #     right = right.next

        # # delete
        # left.next = left.next.next
        return dummy.next

        return dummy.next
