/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (map.size > k) {
      map.delete(nums[i - k - 1]);
      map.set(nums[i], 1);
    }
    if (map.has(nums[i]) && map.size <= k) {
      return true;
    } else {
      map.set(nums[i], 1);
    }
  }
  return false;
};

// seconde way to do it with hashmap:

var containsNearbyDuplicate = function (nums, k) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (i - map.get(nums[i]) <= k) return true;
    else map.set(nums[i], i);
  }
  return false;
};

// instead of setting the value with 1,
// we can set it as the index;
// if map.get(num[i]) exist, means the nums[i] is the duplicate;
// then map.get(nums[i]) will return the first nums[i]'s index in the nums;
