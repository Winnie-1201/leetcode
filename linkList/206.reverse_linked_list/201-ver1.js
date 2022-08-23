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
var reverseList = function (head) {
  let next;
  let prev = null;
  while (head) {
    // bacause we need to reverse the list,
    // then just use head to do the changes
    // next: is the rest of the un-reversed list
    next = head.next;
    // connect the reversed list;
    // at first, the prev is null which lets the
    // next value of first node become null
    head.next = prev;
    // update the reversed list;
    prev = head;
    // update the head;
    head = next;
  }
  return prev;
};

// I worked on it for 10 minutes but did not come
// up with an good idea, so I looked at the discussion;
// finnaly come up with the answer;
//
// The main point for this problem is to use pointers,
// and know how to move the pointers to achieve the goal.
