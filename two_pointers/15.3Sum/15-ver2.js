/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums = nums.sort((a, b) => a - b);
  // console.log(nums)
  let result = [];
  for (let i = 0; i < nums.length - 2; i++) {
    let mid = i + 1;
    let right = nums.length - 1;
    if (i > 0 && nums[i - 1] === nums[i]) continue;
    while (mid < right) {
      let sum = nums[i] + nums[mid] + nums[right];
      if (sum === 0) {
        result.push([nums[i], nums[mid], nums[right]]);
        mid += 1;
        right -= 1;
        while (nums[mid] === nums[mid - 1]) mid++;
        while (nums[right] === nums[right + 1]) right--;
      } else if (sum > 0) right--;
      else {
        mid++;
      }
    }
  }
  return result;
};
