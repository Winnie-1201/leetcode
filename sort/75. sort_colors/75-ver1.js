/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let swrap = false;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] > nums[i + 1]) {
      [nums[i], nums[i + 1]] = [nums[i + 1], nums[i]];
      swrap = true;
    }
  }
  if (!swrap) return nums;
  return sortColors(nums);
};

// var sortColors = function(nums) {
//     if (nums.lenght <= 1) return nums;
//     let arr1 = nums.slice(0, Math.floor(nums.length / 2));
//     let arr2 = nums.slice(Math.floor(nums.length / 2));
//     return merge(arr1, arr2)
// };

// var merge = function (arrA, arrB) {
//     let i = 0;
//     let j = 0;
//     while (i < arrA.length) {
//         if (arrA[i] === arrB[j]) {
//             i++;
//         } else if (arrA[i] > arrB[j]) {
//             a
//         }
//     }
// }

// I tried to use mergesort in place but failed;
// then I used bubble sore, it works but very slow!
// will try new method (mergesort-maybe not that simple;
// maybe try quicksort?) next time;
