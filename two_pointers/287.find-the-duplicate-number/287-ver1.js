/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
  let sorted = nums.sort((a, b) => a - b);
  for (let i = 0; i < sorted.length - 1; i++) {
    if (nums[i] === nums[i + 1]) return nums[i];
  }
  // for (let i = 0; i < nums.length - 1; i++) {
  //     if (nums.slice(i + 1).includes(nums[i])) return nums[i];
  // }
};

// it works but takes O(nlogn) or O(n) space;
// next time:
// 1. loop through the nums, get the value on nums[i];
// 2. mark that value;
// 3. if that value shows second time, return it;
// because there are only n distinct numbers and the length of nums is n+1;
