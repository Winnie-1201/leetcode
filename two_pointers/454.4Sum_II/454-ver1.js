/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
var fourSumCount = function (nums1, nums2, nums3, nums4) {
  let count = 0;
  let sum1 = [];
  for (let i = 0; i < nums1.length; i++) {
    for (let j = 0; j < nums2.length; j++) {
      sum1.push(nums1[i] + nums2[j]);
    }
  }
  let sum2 = [];
  for (let i = 0; i < nums3.length; i++) {
    for (let j = 0; j < nums4.length; j++) {
      sum2.push(nums3[i] + nums4[j]);
    }
  }
  for (let i = 0; i < sum1.length; i++) {
    for (let j = 0; j < sum2.length; j++) {
      if (sum1[i] + sum2[j] === 0) count++;
    }
  }
  return count;
};

// only works for few cases;
// with Time Limit Exceeded error;
// next time try to use hashmap!
// learn how to use hashmap on js or java;
