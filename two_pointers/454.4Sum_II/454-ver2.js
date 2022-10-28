/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
var fourSumCount = function (nums1, nums2, nums3, nums4) {
  let count = 0;
  let sum1 = new Map();
  for (let i = 0; i < nums1.length; i++) {
    for (let j = 0; j < nums2.length; j++) {
      let sum = nums1[i] + nums2[j];
      sum1.set(sum, sum1.get(sum) + 1 || 1);
    }
  }
  // console.log(sum1)
  for (let i = 0; i < nums3.length; i++) {
    for (let j = 0; j < nums4.length; j++) {
      let sum = -(nums3[i] + nums4[j]);
      count += sum1.get(sum) ? sum1.get(sum) : 0;
    }
  }

  return count;
};
