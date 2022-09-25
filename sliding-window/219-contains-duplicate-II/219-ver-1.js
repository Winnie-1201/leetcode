/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  for (let i = 0; i < nums.length - 1; i++) {
    let j = i + 1;
    while (j - i <= k) {
      if (nums[i] === nums[j]) return true;
      j++;
    }
  }
  return false;
};

// only works for few cases and has time exceed for large array;
// next time try:
// 1. hash map:
//     - define hashmap = {}
//     - loop through the array, if nums[i] exist in hashmap, return true, else add it
// 2. sliding window:
//     - define a map = new Map();
//     - loop through, add new num to the map,
//     - if size > k, delete the leftmost which is the first one
//     - if map has the num, return true;
