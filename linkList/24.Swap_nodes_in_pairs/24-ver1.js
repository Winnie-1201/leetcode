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

var swapPairs = function (head) {
  let dummy = new ListNode(-1);
  dummy.next = head;
  prev = dummy;

  while (head && head.next) {
    let curr = head;
    let nxt = head.next;

    //swap:
    prev.next = nxt;
    curr.next = nxt.next;
    nxt.next = curr;

    prev = curr;
    head = curr.next;
  }

  return dummy.next;
};
