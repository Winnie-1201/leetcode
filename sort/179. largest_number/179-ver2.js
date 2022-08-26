/**
 * @param {number[]} nums
 * @return {string}
 */

//  - the number with larger leading digit go first;
//  - the numbers have the same leading digit
//      - have same digit length :
//          - the larger number goes first
//      - do not have the same digit length:
//          - the one with less digit would go first

var largestNumber = function (nums) {
  let isAllZero = true;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      isAllZero = false;
      break;
    }
  }
  if (isAllZero) return "0";
  nums.sort(customSort);
  return nums.join("");
};

var customSort = function (a, b) {
  let m = String(a);
  let n = String(b);
  if (m + n > n + m) return -1;
  else if (m + n < n + m) return 1;
  return 0;
};
// var findMax = function(nums) {
//     let max = String(nums[0]).split("")[0];
//     let idx = 0;
//     for (let i = 1; i < nums.length; i++) {
//         let nxt = String(nums[i]).split("")[0];
//         if (Number(nxt) > Number(max)) {
//             max = nxt;
//             idx = i;

//         }
//     }
//     return idx;
// }

// the second time I still cannot get the answer;
// so I read the solution and the discussion found out
// we can use the built in sort for this question
// in the built in sort, we sort it as a string like
// if m+n > n+m then we will rank m+n first which returns -1
