/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let len = nums1.length + nums2.length;
  let mid = Math.floor(len / 2);
  let arr = [];
  let i = 0;
  let j = 0;
  // if (nums1.length === 0) return nums2[0];
  // else if (nums2.length === 0) return nums1[0];
  while (arr.length <= mid) {
    if (nums1[i] <= nums2[j]) {
      arr.push(nums1[i]);
      i++;
    } else {
      arr.push(nums2[j]);
      j++;
    }
  }
  if (len % 2 !== 0) return arr[arr.length - 1];
  else {
    return (arr[arr.length - 1] + arr[arr.length - 2]) / 2;
  }
};

// /**
//  * @param {number[]} nums1
//  * @param {number[]} nums2
//  * @return {number}
//  */
//  var findMedianSortedArrays = function(nums1, nums2) {
//     let len = nums1.length + nums2.length;
//     let mid = Math.floor(len / 2)
//     let arr = [];
//     let i = 0;
//     let j = 0;
//     if (nums1.length === 0) {
//         if (len % 2 === 0) return (nums2[mid - 1] + nums2[mid])/2
//         else return nums2[mid];
//     } else if (nums2.length === 0) {
//         if (len % 2 === 0) return (nums1[mid - 1] + nums1[mid])/2
//         else return nums1[mid];
//     }
//     while (arr.length <= mid) {
//         if (nums1[i] < nums2[j]) {
//             arr.push(nums1[i]);
//             i++;
//             if (i === nums1.length) arr.push(nums2[j])
//         } else {
//             arr.push(nums2[j]);
//             j++;
//             if (j === nums2.length) arr.push(nums1[i])
//         }
//     }
//     if (len % 2 !== 0) return arr[arr.length - 1];
//     else {
//         return (arr[arr.length - 1] + arr[arr.length - 2])/2
//     }
// };

// Only works for some tests;
// the problem asks for O(lon(m+n)) runtime,
// But I did not figure out how to do it with that runtime;
//
// after looking at the discussion:
// 1. use built in sort but that would have O(nlogn);
// 2. use merge sort to make a sorted array;
