/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let max = 0;
  let sum = 0;
  let start = 0;
  for (let end = 0; end < nums.length; end++) {
    sum += nums[end];
    if (end - start - k >= sum) {
      max = max > end - start ? max : end - start;
      sum -= nums[start];
      start++;
    }
    max = max > end - start + 1 ? max : end - start + 1;
  }
  return max;
};
