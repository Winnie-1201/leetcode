/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  let i = 0;
  let j = 0;
  while (j < nums.length) {
    if (nums[i] === val && nums[j] !== val) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
      j++;
    } else if (nums[i] === val && nums[j] === val) {
      j++;
    } else {
      i++;
      j++;
    }
  }
  return i;
};
