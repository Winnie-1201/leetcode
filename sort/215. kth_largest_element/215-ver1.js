/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  let max = nums[0];
  let pre_max = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] >= max) {
      pre_max = max;
      max = nums[i];
    }
  }
  return pre_max;
};

// the above does not work; did not use k;
// Works but not efficient, took so much time to run
// and the problem asks for O(n) runtime;
// what I had is O(n^2);

// var findKthLargest = function(nums, k) {
//     let res;
//     while (k > 0) {
//         let max = nums[0];
//         let idx = 0;
//         for (let i = 1; i < nums.length; i++) {
//             if (nums[i] > max) {
//                 max = nums[i]
//                 idx = i;
//             }
//         }
//         res = max;
//         nums.splice(idx, 1)
//         k--;
//     }
//     return res;
// };

// after reading the discussion, it may need to use heap which
// is something I do not know.
// for next try, learn more about heap
