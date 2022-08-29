/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums = nums.sort((a, b) => a - b);
  let start = 0;
  let end = nums.length - 1;
  let res = [];
  while (start < end) {
    let remainder = nums[end] + nums[start];
    for (let i = start + 1; i < end; i++) {
      let arr = [nums[start], nums[i], nums[end]];
      if (nums[i] + remainder === 0) {
        res.push(arr);
      }
    }
    if (Math.abs(nums[start]) > Math.abs(nums[end])) start++;
    else end--;
  }

  const setArray = new Set(res.map((x) => JSON.stringify(x)));

  const uniqArray = [...setArray].map((x) => JSON.parse(x));

  return uniqArray;
};

// does not work because I have the start and end both changed
// when found the triplets for start and end pair
// which should move one then check and move the other one then check;
//
// next time:
// 1. loop through the array with i;
// 2. for each i, check all the ele from i - arr.length to see if
//    there are any pair would sum(i+pair) === 0;
//    - also when i === i + 1 skip this i because it is the duplicates
