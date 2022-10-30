/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function (head) {
  let arr1 = [head.val];
  let arr2 = [];
  let curr = head;
  let center = head;
  while (curr.next.next) {
    center = center.next;
    arr1.unshift(center.val);
    curr = curr.next.next;
  }
  // center = center.next;
  while (center.next) {
    arr2.push(center.next.val);
    center = center.next;
  }

  let max = 0;
  // console.log(arr1, arr2)
  for (let i = 0; i < arr1.length; i++) {
    if (max < arr1[i] + arr2[i]) max = arr1[i] + arr2[i];
  }
  return max;
};

// works but very slow and took so much space!

// why did I just use one array...?
var pairSum = function (head) {
  let arr = [head.val];
  let max = 0;
  while (head.next) {
    head = head.next;
    arr.push(head.val);
  }

  // let right = Math.floor(arr.length / 2)
  for (let i = 0; i < arr.length / 2; i++) {
    if (max < arr[i] + arr[arr.length - i - 1])
      max = arr[i] + arr[arr.length - i - 1];
  }

  return max;
};
