/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  let sum = 0;
  let maxAvg = -Infinity;
  if (nums.length <= 1) return nums[0];
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    // console.log(sum)
    if (i >= k - 1) {
      maxAvg = Math.max(maxAvg, sum / k);
      // console.log(nums[i - k + 1])
      sum = sum - nums[i - k + 1];
    }
  }
  return maxAvg;
};

// be careful when declare max or min values;
// it is better to use infinity than 0;
