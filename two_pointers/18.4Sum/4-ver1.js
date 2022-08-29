/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
  nums = nums.sort((a, b) => a - b);
  let start = 0;
  let end = nums.length - 1;
  let res = [];
  while (start < end) {
    let max = 0;
    let min = Infinity;
    let left = start + 1;
    let right = end - 1;
    while (left < right) {
      let sum = nums[start] + nums[left] + nums[right] + nums[end];
      if (sum > max) max = sum;
      if (sum < min) min = sum;
      if (sum === target) {
        res.push([nums[start], nums[left], nums[right], nums[end]]);
        left++;
        right--;
      } else if (sum < target) {
        left++;
        if (nums[left] === nums[left - 1]) left++;
        // if (sum > max) max = sum;
      } else {
        right--;
        if (nums[right] === nums[right - 1]) right--;
        // if (sum > max) max = sum;
      }
    }
    if (max === target || min === target) {
      start++;
      end--;
    } else if (res.length > 0 && Math.abs(nums[start]) > Math.abs(nums[end])) {
      start++;
      if (nums[start] === nums[start - 1]) start++;
    } else if (min > target || max - min > target) end--;
    else start++;
  }
  return res;
};

// works for some cases but there is something wrong with my logic;
// I did not cover all of the situations
// need to work on the logic next time:
// how to move each pointers based on the relationship bettween
// the value of their sum and the target!
