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

// from solution:
// recursive binary search
/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  return helper(0, nums.length - 1, nums);
};

var helper = function (left, right, nums) {
  if (left === right) return left;
  let mid = Math.floor((left + right) / 2);
  // if (nums[i] < nums[i+1]) then we only need to check i+1 and i+2
  if (nums[mid] <= nums[mid + 1]) return helper(mid + 1, right, nums);
  else return helper(left, mid, nums);
};

// iterate binary search
var findPeakElement = function (nums) {
  // return helper(0, nums.length - 1, nums)
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    // if (left === right) return left;
    if (nums[mid] < nums[mid + 1]) left = mid + 1;
    else right = mid;
  }
  return left;
};
