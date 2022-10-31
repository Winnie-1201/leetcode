/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function (node) {
  //     let prev;
  //     let curr = node;
  //     while (curr.next) {
  //         prev = curr;
  //         curr.val = curr.next.val;
  //         curr = curr.next;
  //     }
  //     prev.next = null;

  let nxt = node.next;
  node.val = nxt.val;
  node.next = nxt.next;
  nxt.next = null;
  delete nxt;
};
