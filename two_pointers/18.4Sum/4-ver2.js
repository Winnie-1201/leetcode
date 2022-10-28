/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
  nums = nums.sort((a, b) => a - b);
  let result = [];
  for (let i = 0; i < nums.length - 3; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    for (let start = i + 1; start < nums.length - 2; start++) {
      let left = start + 1;
      let right = nums.length - 1;
      if (start > i + 1 && nums[start] === nums[start - 1]) continue;
      while (left < right) {
        let sum = nums[i] + nums[start] + nums[left] + nums[right];
        if (sum === target) {
          result.push([nums[i], nums[start], nums[left], nums[right]]);
          left++;
          right--;
          while (nums[left] === nums[left - 1]) left++;
          while (nums[right] === nums[right + 1]) right--;
        } else if (sum < target) left++;
        else right--;
      }
    }
  }
  return result;
};
