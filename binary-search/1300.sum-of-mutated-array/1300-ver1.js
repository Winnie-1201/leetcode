/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var findBestValue = function (arr, target) {
  arr = arr.sort((a, b) => a - b);
  if (target / arr.length < arr[0]) return target / arr.length;

  let left = 0;
  let right = arr.length - 1;
  while (left < right - 1) {
    let mid = Math.floor((left + right) / 2);
    // console.log(mid)
    if (arr[mid] * arr.length === target) return arr[mid];
    else if (arr[mid] * arr.length > target) {
      // console.log("f")
      // if (right = left + 1) {
      //     return (target - arr[left] * (left+1)) / (arr.length - right)
      // }
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  // console.log(arr, left)
  // if (left === arr.length - 1) return arr[left]
  let up = Math.ceil(
    (target - arr[left] * (left + 1)) / (arr.length - left - 1)
  );

  let down = Math.floor(
    (target - arr[left] * (left + 1)) / (arr.length - left - 1)
  );

  let sum1 = arr[left] * (left + 1) + up * (arr.length - left - 1);
  let sum2 = arr[left] * (left + 1) + down * (arr.length - left - 1);

  if (Math.abs(sum1 - target) < Math.abs(sum2 - target)) {
    return Math.abs(sum1 - target) < Math.abs(arr[left] * arr.length - target)
      ? up
      : arr[left];
  } else {
    return Math.abs(sum2 - target) < Math.abs(arr[left] * arr.length - target)
      ? down
      : arr[left];
  }
};

// it only works for few cases;
// I did this case by case so it will not pass all tests...

// solution from others
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var findBestValue = function (arr, target) {
  var findSum = function (mid) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
      sum += arr[i] < mid ? arr[i] : mid;
    }
    return sum;
  };

  let left = 0;
  let right = Math.max(...arr);
  let res = 1;
  let diff = Infinity;

  while (left <= right) {
    //left and right are not index
    let mid = Math.floor((left + right) / 2);
    if (findSum(mid) < target) left = mid + 1;
    else right = mid - 1;

    if (
      Math.abs(findSum(mid) - target) < diff ||
      (Math.abs(findSum(mid) - target) === diff && mid < res)
    ) {
      res = mid;
      diff = Math.abs(findSum(mid) - target);
      // console.log(res, diff)
    }
  }
  return res;
};

// did not use left and right as the index;
// since this problem can return the value that is not in the array;
// and it only needs the sum that is closest to the target;
