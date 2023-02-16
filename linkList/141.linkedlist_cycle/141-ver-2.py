# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #         nodeList = set()
        #         currNode = head

        #         while currNode:
        #             nodeList.add(currNode)
        #             currNode = currNode.next

        #             if currNode in nodeList:
        #                 return True
        slow = fast = head

        # Floyd's cycle detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
