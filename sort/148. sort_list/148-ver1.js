/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function (head) {
  let currNode = head;
  let swrap = false;
  while (currNode.next) {
    if (currNode.val > currNode.next.val) {
      [currNode.val, currNode.next.val] = [currNode.next.val, currNode.val];
      swrap = true;
      currNode = currNode.next;
    }
    currNode = currNode.next;
  }
  if (!swrap) return head;
  else return sortList(head);
};

// tried to use bubble sort but getting error with
// currNode.next -- Runtime Error;

// Suppose to use MergeSort
