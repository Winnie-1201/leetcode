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
  let count = 0;
  let start = head;
  let end;
  let mid;
  let curr = head;
  if (left === right) return head;
  while (count < right && curr) {
    count++;
    if (count === left - 1) {
      mid = curr.next;
      curr.next = null;
      curr = mid;
    } else if (count === right - 1) {
      end = curr.next;
      curr.next = null;
    }
    curr = curr.next;
  }
  let reverse = reverseList(mid);
  curr = head;
  while (curr.next) {
    curr = curr.next;
  }
  curr.next = reverse;
  curr = reverse;
  while (curr.next) {
    curr = curr.next;
  }
  curr.next = end;
  return head;
  // let count = 1;
  // let tail = head;
  // while (count < left) {
  //     count++;
  //     tail = tail.next;
  // }
  // let cur = head;
  // while (count < left - 1) {
  //     count++;
  //     tail = tail.next;
  // }
};

var reverseList = function (head) {
  let prev = null;

  while (head) {
    let nxt = head.next;
    head.next = prev;
    prev = head;
    head = nxt;
  }
  return prev;
};

// it only works for some cases but not
// the edge cases
//
// it is also about pointers;
// use the pointers to mutate the linked list
