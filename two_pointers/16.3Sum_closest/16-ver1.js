/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  nums = nums.sort((a, b) => a - b);
  let cSum = nums[0] + nums[1] + nums[2];
  let start = 0;
  for (let i = 0; i < nums.length; i++) {
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];
      let temp = Math.abs(cSum - target);
      if (sum - target === 0) return sum;
      else if (Math.abs(sum - target) < temp) {
        cSum = sum;
        if (sum < target) left++;
        else right--;
      } else {
        if (sum < target) left++;
        else right--;
      }
    }
  }
  return cSum;
};
