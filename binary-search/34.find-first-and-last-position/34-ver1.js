/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;
  let start = nums[left] === target ? left : -1;
  let end = nums[right] === target ? right : -1;
  let mid;
  let test = false;
  while (left <= right) {
    if (nums[left] === target && start === -1) start = left;
    if (nums[right] === target && end === -1) end = right;
    mid = Math.floor((left + right) / 2);
    if (nums[mid] < target) {
      left = mid + 1;
    } else if (nums[mid] > target) {
      right = mid - 1;
    } else {
      test = true;
      end = end <= end ? end : mid;
      start = start <= mid ? start : mid;
      left++;
      right--;
    }
  }
  if (start === -1 && test) start = mid;
  if (end === -1 && test) end = mid;

  return [start, end];
};

// for next time:
// try to write the helper funciton
