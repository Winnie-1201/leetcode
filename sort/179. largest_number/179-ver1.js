/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function (nums) {
  let str = "";
  while (nums.length > 0) {
    let min = findMin(nums);
    str += min[0];
    nums.splice(min[1], 1);
  }
  return str;
};

var findMin = function (nums) {
  let min = nums[0];
  let idx = 0;
  for (let i = 1; i < nums[i]; i++) {
    if (nums[i] % 10 > min % 10) {
      min = nums[i];
      idx = i;
    }
  }
  return [min, idx];
};

// Passed some of the test;
// but getting wrong answer for case:
// input:    [34323,3432]
// output:   "34323 3432"
// expected: "3432 34323"
// it seems like:
//   - the number with larger leading digit go first;
//   - the numbers have the same leading digit
//      - have same digit length :
//          - the larger number goes first
//      - do not have the same digit length:
//          - the one with less digit would go first
// will try it later;
