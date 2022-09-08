/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  let nodeList = [];
  let curr = head;
  while (curr) {
    if (!nodeList.includes(curr)) {
      nodeList.push(curr);
      curr = curr.next;
    } else return curr;
  }
  return null;
};

// it works
// or use set
var detectCycle = function (head) {
  if (!head) return null;

  const listSet = new Set();
  let current = head;

  while (current) {
    if (listSet.has(current)) return current;
    listSet.add(current);
    current = current.next;
  }

  return null;
};
