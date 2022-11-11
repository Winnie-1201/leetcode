# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
 #         find the mid
        temp = ListNode()
        temp.next = head
        mid = temp
        while temp and temp.next:
            temp = temp.next.next
            mid = mid.next
        mid = mid.next


#       reverse the mid
        prev = None
        curr = mid
        nxt = curr
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while head and prev:
            print(head.val, prev.val)
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        # if not head and not mid: return True
        return True

# another way:
        # slow, fast, prev = head, head, None
        # #  find the mid
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        # prev, slow, prev.next = slow, slow.next, None

        # # reverse the second half:
        # # the order matters!
        # while slow:
        #     slow.next, prev, slow = prev, slow, slow.next
        # fast, slow = head, prev

        # while slow:
        #     if slow.val != fast.val: return False
        #     slow, fast = slow.next, fast.next
        # return True
