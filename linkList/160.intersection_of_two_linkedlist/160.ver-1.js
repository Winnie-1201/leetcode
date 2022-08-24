/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
  // currA would be the one with larger length;
  let currA = null;
  let currB = null;

  let lengthA = getLength(headA);
  let lengthB = getLength(headB);

  let lenDiff;

  if (lengthA >= lengthB) {
    lenDiff = lengthA - lengthB;
    currA = headA;
    currB = headB;
  } else {
    lenDiff = lengthB - lengthA;
    currA = headB;
    currB = headA;
  }
  while (lenDiff > 0) {
    currA = currA.next;
    lenDiff--;
  }
  while (currA) {
    if (currA === currB) return currA;
    else {
      currA = currA.next;
      currB = currB.next;
    }
  }
};

var getLength = function (head) {
  let length = 0;
  let curr = head;
  while (curr) {
    length++;
    curr = curr.next;
  }
  return length;
};

// I got the above idea after reading the dicussion;
// next time with such problem, try to think about the helper function;
// I first did think about the length of the list but
// I did not think about the helper
//
// The below was what i had which only worked for few cases;
// var getIntersectionNode = function(headA, headB) {
//     let currA = headA;
//     let currB = headB;
//     if (!currA || !currB || !currA.next || !currB.next) return 0;
//     while (currA.next && currB.next) {
//         if (currA === currB) {
//             return currA
//         } else if (currA === currB.next) {
//             return currB.next;
//         } else if (currA.next === currB) {
//             return currA.next;
//         } else {
//             currA = currA.next;
//             currB = currB.next;
//         }
//     }
//     return 0;
// };
