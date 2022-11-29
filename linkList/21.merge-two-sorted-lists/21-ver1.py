# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        result = temp
        if not list1 or not list2:
            return list1 or list2
        while list1 and list2:
            if list1.val >= list2.val:
                temp.next = list2
                # temp = temp.next
                list2 = list2.next
            else:
                temp.next = list1
                # temp = temp.next
                list1 = list1.next
            temp = temp.next
        temp.next = list1 or list2
        # if not list1:
        #     temp.next = list2
        # elif not list2:
        #     temp.next = list1

        return result.next
