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
var oddEvenList = function (head) {
  let temp;
  if (!head || !head.next || !head.next.next) return head;
  let start = head;
  let nxt = head.next;
  let prev = nxt;
  while (start.next && nxt.next) {
    // temp = start;
    start.next = nxt.next;
    start = nxt.next;
    nxt.next = start.next;
    nxt = nxt.next;
    temp = start;
  }
  temp.next = prev;
  return head;
};

// First time I passed all the tests for linked list!!!
// without looking for any hints!!
// Sooo excited!
// feel like:
// Linked list problem is all about pointers!
// we assign pointers to point at different node,
// and through changing the pointers to mutate the list;
// after doing the thing, change the pointers to point to its next value
// then we can traverse the whole list;
//
// the runtime is good and the memory is good!!
// and I am good too hahaha!!!
