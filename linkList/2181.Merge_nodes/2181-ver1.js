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
var mergeNodes = function (head) {
  head = head.next;
  let curr = head;
  let temp = head;
  let sum = 0;
  let prev;

  while (curr && curr.next) {
    sum += curr.val;
    curr = curr.next;

    if (curr.val === 0) {
      temp.val = sum;
      prev = temp;
      temp = temp.next;
      sum = 0;
    }
  }

  prev.next = null;
  return head;
};
