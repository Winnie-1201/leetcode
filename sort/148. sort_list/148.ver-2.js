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
var sortList = function (head) {
  if (!head || !head.next) return head;
  let curr = head;
  let startA = null;
  while (head && head.next) {
    startA = startA === null ? head : startA.next;
    head = head.next.next;
  }
  let nxt = startA.next;
  startA.next = null;
  return mergeList(sortList(curr), sortList(nxt));
};

// var getMid(head) {
//     let midPrev = null;
//     while (head && head.next) {

//     }
// }
var mergeList = function (headA, headB) {
  let res = new ListNode();
  let temp = res;
  while (headA && headB) {
    // let nxtA = new ListNode(headA.val);
    // let nxtB = new ListNode(headB.val);
    if (headA.val > headB.val) {
      temp.next = headB;
      headB = headB.next;
      // if (!headB) {
      //     temp = temp.next;
      //     temp.next = headA;
      // }
      temp = temp.next;
    } else {
      temp.next = headA;
      headA = headA.next;
      // if (!headA) {
      //     temp = temp.next;
      //     temp.next = headB;
      // }
      temp = temp.next;
    }
  }
  temp.next = headA !== null ? headA : headB;
  return res.next;
};

// var sortList = function(head) {
//     if (!head || !head.next) return head;
//     let swrap = false;
//     let curr = head;
//     while (curr) {
//         if (curr.next && curr.val > curr.next.val) {
//             [curr.val, curr.next.val] = [curr.next.val, curr.val];
//             curr = curr.next;
//             swrap = true;
//         }
//         curr = curr.next;
//     }
//     if (!swrap) return head;
//     return sortList(head);
// };

// I first fixed my bubble sort and it works okay;
// then regarding as the solution, i tried the mergesort and
// it also works, for mergeSort, we need:
// 1. a getMid helper function which can help us get the middle node
//    of the given linked list
// 2. a merge helper funtion which can help us to merge two given
//    linked list
// 3. then inside of the sortList function, we can first call the
//    the getMid function to get the first mid, then sort the two list:
//    a) head -> mid; b) mid -> the end
//    recursively;
// 4. after that, just return the merge function on the two sorted list;
