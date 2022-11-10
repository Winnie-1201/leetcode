# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # tempA = set()
        # curr = headA
        # while curr:
        #     tempA.add(curr)
        #     curr = curr.next
        # curr = headB
        # while curr:
        #     if curr in tempA: return curr
        #     curr = curr.next
        # return None
        a = headA
        b = headB

        while a != b:
            # append b to a when a is none
            a = headB if not a else a.next
            # append a to b when b is none
            # then the two linked list would have the same len
            # when they are both none, means there is no intersection
            b = headA if not b else b.next
        return a
