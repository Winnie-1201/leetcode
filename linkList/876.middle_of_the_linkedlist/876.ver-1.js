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
var middleNode = function (head) {
  let mid = head;
  while (head != null && head.next != null) {
    // let size be the [head.vals];
    // everytime the size increased by 2, the mid
    // would increase by 1;
    head = head.next.next;
    mid = mid.next;
  }
  return mid;
  //     let count = 0;
  //     let currNode = head;
  //     if (!head || !head.next) return head;
  //     while (currNode) {
  //         count++;
  //         currNode = currNode.next;
  //     }
  //     let mid = Math.floor(count/2);
  //     while (head) {
  //         mid--;
  //         head = head.next;
  //         if (mid === 0) return head;
  //     }
};

// the bottom method is what I wrote, it works but slow;
//
// the top one is other people wrote;
//
