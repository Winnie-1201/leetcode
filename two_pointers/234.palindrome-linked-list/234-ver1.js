/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  let arr = [];
  if (!head) return false;
  while (head) {
    arr.push(head.val);
    head = head.next;
  }
  let start = 0;
  let end = arr.length - 1;
  while (start < end) {
    if (arr[start] !== arr[end]) return false;
    start++;
    end--;
  }
  return true;
};

// it works
// next time:
// use a slow and fast pointer
// 1. to find the middle point: use slow = slow.next, fast = fast.next.next
//     slow would be the middle point
// 2. define a reverse function to reverse the second half linked list
//      use prev, next, head
// 3. compare if the first half and the reversed second half is the same
