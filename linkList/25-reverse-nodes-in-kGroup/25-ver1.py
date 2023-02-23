# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # needs to modify the head, so need a dummy
        dummy = ListNode(0, head)
        # needs to store the previous node of a group
        groupPrev = dummy

        while True:
            # get the kth node which is the end of the group
            kth = self.getKth(groupPrev, k)

            # if not k, then there is no more groups
            if not kth:
                break

            # get the next node of k which is the start of another group
            groupNext = kth.next

            # reversing the group
            # prev needs to point to the start of next group
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # after the group is reversed,
            # needs to change the groupPrev
            temp = groupPrev.next
            # when the group is reverse, the started node should be changed
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
