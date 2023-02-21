# Definition for singly-linked list.
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergeList.append(self.merge(l1, l2))

            lists = mergeList

        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
#         sortedList = ListNode()
#         temp = sortedList

#         while l1 or l2:
#             if l1 and l2 and l1.val <= l2.val:
#                 node = ListNode(l1.val)
#                 temp.next = node
#                 l1 = l1.next
#                 temp = temp.next
#             elif l1 and l2 and l1.val > l2.val:
#                 node = ListNode(l2.val)
#                 temp.next = node
#                 l2 = l2.next
#                 temp = temp.next
#             else:
#                 temp.next = l1 if l1 else l2
#                 l1 = l2 = None

#         return sortedList.next
