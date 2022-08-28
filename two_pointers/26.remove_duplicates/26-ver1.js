/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let start = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[start]) {
      start++;
      [nums[i], nums[start]] = [nums[start], nums[i]];
    }
  }
  return start + 1;

  //method 2:
  // let start = 0;
  // while (start < nums.length - 1) {
  //     if (nums[start] === nums[start + 1]) {
  //         nums.splice(start + 1, 1);
  //     } else {
  //         start++;
  //     }
  // }
  // return nums.length;
};

// Both of them work but the first one is much faster;
