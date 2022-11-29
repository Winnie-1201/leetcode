/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (nums) {
  let left = 0;
  let right = nums.length;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] !== nums[mid + 1] && nums[mid] !== nums[mid - 1])
      return nums[mid];
    else if (nums[mid] !== nums[mid + 1] && mid % 2 !== 0) left = mid + 1;
    else if (nums[mid] === nums[mid + 1] && mid % 2 === 0) left = mid + 1;
    else right = mid - 1;
  }
  return nums[left];
};
