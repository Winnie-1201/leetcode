/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let nodeList = [];
  let curr = head;
  while (curr) {
    nodeList.push(curr);
    curr = curr.next;
    if (nodeList.includes(curr)) return true;
  }
  return false;
};

// the above codes is what I wrote;
// it works but very slow and take n memory;

// the below is what other people wrote;
//
// if two nodes in a cycle, they will eventually meet;
// var hasCycle = function(head) {
//     let curr = head;
//     while (curr && curr.next) {
//         head = head.next;
//         curr = curr.next.next;
//         if (curr === head) return true;
//     }
//     return false;
// };
