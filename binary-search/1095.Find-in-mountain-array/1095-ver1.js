/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * function MountainArray() {
 *     @param {number} index
 *     @return {number}
 *     this.get = function(index) {
 *         ...
 *     };
 *
 *     @return {number}
 *     this.length = function() {
 *         ...
 *     };
 * };
 */

/**
 * @param {number} target
 * @param {MountainArray} mountainArr
 * @return {number}
 */
var findInMountainArray = function (target, mountainArr) {
  let left = 0;
  let right = mountainArr.length() - 1;

  // find the mountain peak index
  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (mountainArr.get(mid) < mountainArr.get(mid + 1)) left = mid + 1;
    else right = mid;
  }

  let Mtindex = left;

  // split the array and binary search both
  let r = Mtindex;
  let l = 0;
  while (l <= r) {
    let mid1 = Math.floor((l + r) / 2);
    if (mountainArr.get(mid1) === target) return mid1;
    else if (mountainArr.get(mid1) > target) r = mid1 - 1;
    else l = mid1 + 1;
  }

  l = Mtindex + 1;
  r = mountainArr.length() - 1;
  while (l <= r) {
    mid1 = Math.floor((l + r) / 2);
    if (mountainArr.get(mid1) === target) return mid1;
    else if (mountainArr.get(mid1) < target) r = mid1 - 1;
    else l = mid1 + 1;
  }

  return -1;
};
