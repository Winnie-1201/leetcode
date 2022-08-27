/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    if (nums.slice(i + 1).includes(target - nums[i]))
      return [i, nums.indexOf(target - nums[i], i + 1)];
  }
  // for (let i = 0; i < nums.length - 1; i++) {
  //     for (let j = i + 1; j < nums.length; j++) {
  //         if (nums[i] + nums[j] === target) return [i, j]
  //     }
  // }
};

// Both of the method works!
