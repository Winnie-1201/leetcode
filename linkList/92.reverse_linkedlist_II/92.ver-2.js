/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */

var reverseBetween = function (head, left, right) {
  if (!head || !head.next) return head;
  let dummy = new ListNode();
  dummy.next = head;
  let pre = dummy;
  for (let i = 0; i < left - 1; i++) {
    pre = pre.next;
  }
  let start = pre.next;
  let nxt = start.next;
  for (let i = 0; i < right - left; i++) {
    start.next = nxt.next;
    nxt.next = pre.next;
    pre.next = nxt;
    nxt = start.next;
  }
  return dummy.next;
};

// to mutate the linkedlist, we use pointers and they would look like:
// a.next = b.bext;
// b.next = c.next;
// c.next = d.next;
// d = a.next;
// mostly looks like a cycle;

// for the edges cases like the linkedlist only has two node
// but we have three or more pointers, we need to create a
// dummy list that contains an empty node at the begining of the list
// to make sure the method would also works for the edge case;
