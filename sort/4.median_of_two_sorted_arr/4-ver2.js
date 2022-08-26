/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let sorted = [];
  let len = nums1.length > nums2.length ? nums2.length : nums1.length;
  while (nums1.length > 0 && nums2.length > 0) {
    if (nums1[0] < nums2[0]) {
      sorted.push(nums1.splice(0, 1)[0]);
    } else {
      sorted.push(nums2.splice(0, 1)[0]);
    }
  }
  nums1.length > 0 ? sorted.push(...nums1) : sorted.push(...nums2);
  let length = sorted.length;
  if (length % 2 === 1) return sorted[Math.floor(length / 2)];
  return (sorted[length / 2 - 1] + sorted[length / 2]) / 2;
};

// Works perfect!!
