/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let len = 0;
  let curr = head;
  while (curr) {
    len++;
    curr = curr.next;
  }
  let idx = len - n;
  let prev = head;
  let nxt = prev.next;
  if (idx === 0) {
    head = nxt;
    return head;
  }
  while (nxt) {
    idx--;
    if (idx <= 0) {
      prev.next = nxt.next;
      nxt.next = null;
      break;
    } else {
      prev = nxt;
      nxt = nxt.next;
    }
  }
  return head;
};

// it works!!
// next time:

// use two pointers: fast and slow;
// use n to find the fast node;
// then slow to mutate the list
