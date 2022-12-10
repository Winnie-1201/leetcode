# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        lst2 = []

        while l1:
            lst1.append(l1.val)
            l1 = l1.next
        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        res = []
        count = 0
        while lst1 and lst2:
            s = lst1.pop() + lst2.pop() + count
            count = 0
            if s >= 10:
                res.append(s % 10)
                count = s // 10

            else:
                res.append(s)

        if lst1:
            while lst1:
                s = lst1.pop() + count
                count = 0
                if s >= 0:
                    res.append(s % 10)
                    count = s // 10
                else:
                    res.append(s)
            # lst1[len(lst1)-1] = lst1[len(lst1)-1] + count
            # res.extend(lst1)
        if lst2:
            # lst2[len(lst2)-1] = lst2[len(lst2)-1] + count
            # res.extend(lst2)
            while lst2:
                s = lst2.pop() + count
                count = 0
                if s >= 10:
                    res.append(s % 10)
                    count = s // 10
                else:
                    res.append(s)

        if count > 0:
            res.append(count)

        i = len(res) - 1
        result = ListNode(None)
        temp = result
        while i >= 0:

            temp.next = ListNode(res[i])
            temp = temp.next
            i -= 1
        return result.next


# 1. convert to list
# 2. append the sum to a new list called res
# 3. convert the res to the ListNode
