/**
 * @param {number[]} nums
 * @return {number}
 */

// my version
var findPeakElement = function (nums) {
  for (let i = 1; i < nums.length; i++) {
    if (i === nums.length - 1 && nums[i] > nums[i - 1]) return i;
    else if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) return i;
  }
  return 0;
};

// from solution:
var findPeakElement = function (nums) {
  for (let i = 0; i < nums.length - 1; i++) {
    // if nums[0] < nums[1], then we only need to check if nums[1] > nums[2]
    if (nums[i] > nums[i + 1]) return i;
  }
  // if length === 1: return 0
  return nums.length - 1;
};
