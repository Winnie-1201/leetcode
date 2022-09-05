/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let start = 0;
  let max = 0;
  while (start < nums.length - 1) {
    let count = 0;
    let arr = [];
    let nxt = start + 1;
    if (nums[start] === 0) {
      count++;
    }
    arr.push(nums[start]);
    while (nxt < nums.length) {
      if (nums[nxt] === 0) {
        count++;
        if (count >= k + 1) {
          break;
        }
        arr.push(nums[nxt]);
        nxt++;
      } else {
        if (count >= k + 1) {
          break;
        }
        arr.push(nums[nxt]);
        nxt++;
      }
    }
    max = arr.length > max ? arr.length : max;
    start++;
  }
  return max;
};

// also sliding window problem;
// my method only works for some cases;
